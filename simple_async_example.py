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
    coro1 = do_something()
    coro2 = do_something_else()
    aws = [coro1, coro2]
    results = await asyncio.gather(*aws)
    print(results)


asyncio.run(main())
print("--- %s seconds ---" % (time.time() - start_time))
