import asyncio
import concurrent.futures
import time


async def my_task(task_number: int, seconds: int) -> str:
    """
    A task to do for a number of seconds
    """
    # print('Task:{} is taking {} seconds to complete'.format(
    #     task_number, seconds))
    await asyncio.sleep(seconds)
    return "Task:{} completed".format(task_number)


def my_thread_task(task_number: int, seconds: int) -> any:
    """
    A task to do for a number of seconds
    """
    # print('Task:{} is taking {} seconds to complete'.format(
    #     task_number, seconds))
    time.sleep(seconds)
    return "Task:{} completed".format(task_number)


async def async_event(task_nos: int, event_loop: asyncio.AbstractEventLoop):
    start = time.time()
    print("Creating {} async tasks...".format(task_nos))
    tasks = {event_loop.create_task(my_task(i + 1, (i + 1) % 2)) for i in range(task_nos)}
    await asyncio.gather(*tasks)
    print("Time taken for async execution:", time.time() - start)
    # print([t.result() for t in tasks])


def thread_event(task_nos: int) -> concurrent.futures.Future:
    start = time.time()
    print("Creating {} thread tasks...".format(task_nos))
    with concurrent.futures.ThreadPoolExecutor(thread_name_prefix='Thread') as executor:
        tasks = [executor.submit(my_thread_task, (i + 1), (i + 1) % 2) for i in range(task_nos)]
        # concurrent.futures.wait(tasks)
        for task in concurrent.futures.as_completed(tasks):
            try:
                yield task.result()
            except Exception as ex:
                print(ex)
    print("Time taken for thread execution:", time.time() - start)
    # print([t for t in tasks])


if __name__ == '__main__':
    total_ops = 1000

    # async io
    loop = None
    try:
        loop = asyncio.get_event_loop()
        # asyncio.run(event(task_nos))
        loop.run_until_complete(async_event(total_ops, loop))
    finally:
        loop.close()

    # multi-threading
    for val in thread_event(total_ops):
        pass
        # print(val)
