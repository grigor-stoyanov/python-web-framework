import asyncio
import time

from demo.main.tasks import slow_task


async def worker1():
    await asyncio.sleep(1)
    return 'bread'


async def worker2():
    await asyncio.sleep(2)
    return 'ham'


async def worker3():
    await asyncio.sleep(3)
    return 'lettuce'


def worker4(ingredients):
    print(f'making sandwitch with {ingredients}')


async def main():
    start = time.time()
    sandwich_parts = await asyncio.gather(worker1(), worker2(), worker3())
    worker4(sandwich_parts)
    end = time.time()
    print(f'executed in {end - start} s')


# asyncio.run(main())
slow_task(5)
