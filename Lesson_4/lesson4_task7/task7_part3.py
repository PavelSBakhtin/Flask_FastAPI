import asyncio
import random
import time

start_time = time.time()
processes = []

arr = [random.randint(0, 101) for _ in range(1, 1000001)]


async def arr_sum(arg):
    res = sum(arg)
    print(f"{res} calculated in {time.time() - start_time:.2f} seconds")


async def main():
    tasks = []
    for i in range(5):
        task = asyncio.ensure_future(arr_sum(arr))
        tasks.append(task)
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
