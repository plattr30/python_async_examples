import asyncio
import time

start_time = time.time()


async def do_something():
    print("starting do_something")
    await asyncio.sleep(2)
    print("finishing do_something")
    return "did something"


async def do_something_else():
    print("starting do_something_else")
    await asyncio.sleep(3)
    print("finishing do_something_else")
    return "did something else"


async def main():
    task1 = asyncio.create_task(do_something())
    task2 = asyncio.create_task(do_something_else())
    # await task1
    # await task2
    tasks = [task1, task2]
    results = await asyncio.gather(*tasks)
    print(results)


asyncio.run(main())
print("--- %s seconds ---" % (time.time() - start_time))
