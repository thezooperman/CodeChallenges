import asyncio
import concurrent.futures
import time
import random
import secrets
import traceback


async def my_async_task(task_number: int, seconds: int) -> str:
    """
    A task to do for a number of seconds
    """
    # print('Task:{} is taking {} seconds to complete'.format(
    #     task_number, seconds))

    # cancel the current task when random value hits 5
    random_seed = random.randint(1, 10)
    secret_seed = secrets.choice([i for i in range(1, 11)])
    # print(random_seed, secret_seed, task_number)
    if random_seed == 5 or secret_seed == 5:
        # raise asyncio.CancelledError(task_number)
        asyncio.current_task().cancel()
    await asyncio.sleep(1.0 / task_number)
    return "Task:{} completed".format(task_number)


def my_thread_task(task_number: int, seconds: int) -> any:
    """
    A task to do for a number of seconds
    """
    # print('Task:{} is taking {} seconds to complete'.format(
    #     task_number, seconds))
    time.sleep(1.0 / task_number)
    # print(concurrent.futures.thread.threading.currentThread().getName())
    return "Thread:{} completed".format(task_number)


async def async_event(task_nos: int) -> None:
    start = time.time()
    print("Creating {} async tasks...".format(task_nos))

    # ways to create a task
    # can create from an event loop pre-python 3.7 era

    # event_loop = asyncio.events.get_running_loop()
    # tasks = {event_loop.create_task(my_async_task(i + 1, (i + 1) % 2)) for i in range(task_nos)}

    # or just wrap the async tasks in a sequence and schedule it
    # tasks = {my_async_task(i + 1, (i + 1) % 2) for i in range(task_nos)}

    # wrap with create_task to pass as future object, used in wait or gather
    tasks = {asyncio.create_task(my_async_task(i + 1, (i + 1) % 2)): (i + 1) for i in range(task_nos)}

    # enumerate over the task as soon as they complete
    # order guarantee is not maintained
    # for res in asyncio.as_completed(tasks):
    #     try:
    #         result = await res
    #         print(result)
    #     except (asyncio.CancelledError, asyncio.TimeoutError, Exception) as ce:
    #         print("Traceback: {}".format(res))

    # using wait to wait for tasks and handle exception
    done, pending = await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)
    for task in done:
        try:
            if not task.exception():
                print(task.result())
        except (asyncio.CancelledError, asyncio.TimeoutError, Exception) as er:
            print("Error: Task-{} failed with {}".format(tasks[task], type(er).__name__))

    # clear the pending task set
    for pending_task in pending:
        pending_task.cancel()

    # example for asyncio.gather
    # results = await asyncio.gather(*tasks, return_exceptions=True)  # results contains the completed result
    # returned from the method

    # for task in tasks:
    #     try:
    #         if not task.exception():
    #             print(task.result())
    #     except (asyncio.futures.CancelledError, asyncio.CancelledError, Exception) as ex:
    #         print("Error: Task-{} failed with {}".format(tasks[task], type(ex).__name__))

    print("Time taken for async execution:", time.time() - start)


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
    total_ops = 100000

    # async io
    loop = None
    try:
        # loop = asyncio.get_event_loop()
        asyncio.run(async_event(total_ops))
        # loop.run_until_complete(async_event(total_ops, loop))
    finally:
        pass
        # loop.close()

    # multi-threading
    for val in thread_event(total_ops):
        try:
            print(val)
            pass
        except TimeoutError as ter:
            print(ter)
        except concurrent.futures.CancelledError as cer:
            print(cer)
        except Exception as ex:
            print(ex)
