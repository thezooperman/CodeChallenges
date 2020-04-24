import asyncio
import concurrent.futures
import time


async def my_asynctask(task_number: int, seconds: int) -> str:
    """
    A task to do for a number of seconds
    """
    # print('Task:{} is taking {} seconds to complete'.format(
    #     task_number, seconds))
    await asyncio.sleep(1.0 / task_number)
    return "Task:{} completed".format(task_number)


def my_thread_task(task_number: int, seconds: int) -> any:
    """
    A task to do for a number of seconds
    """
    # print('Task:{} is taking {} seconds to complete'.format(
    #     task_number, seconds))
    time.sleep(seconds)
    return "Task:{} completed".format(task_number)


async def async_event(task_nos: int, event_loop: asyncio.AbstractEventLoop) -> None:
    event_loop = asyncio.events.get_running_loop()
    start = time.time()
    print("Creating {} async tasks...".format(task_nos))
    tasks = {event_loop.create_task(my_asynctask(i + 1, (i + 1) % 2)) for i in range(task_nos)}
    await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    # await asyncio.gather(*tasks)
    # for res in asyncio.as_completed(tasks):
    # print_val(await res)
    # print(await res)
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
            except Exception as x:
                print(x)
    print("Time taken for thread execution:", time.time() - start)
    # print([t for t in tasks])


if __name__ == '__main__':
    total_ops = 1000

    # async io
    loop = None
    try:
        # loop = asyncio.get_event_loop()
        asyncio.run(async_event(total_ops, None))
        # loop.run_until_complete(async_event(total_ops, loop))
    finally:
        pass
        # loop.close()

    # multi-threading
    for val in thread_event(total_ops):
        try:
            # print(val)
            pass
        except TimeoutError as ter:
            print(ter)
        except concurrent.futures.CancelledError as cer:
            print(cer)
        except Exception as ex:
            print(ex)
