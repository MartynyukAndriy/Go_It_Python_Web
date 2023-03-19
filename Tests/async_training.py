import asyncio

from time import time

from typing import Coroutine, Any


async def coro1() -> Coroutine[Any, Any, str]:
    await asyncio.sleep(1.5)
    return "Hello"


async def coro2():
    await asyncio.sleep(1)
    return "World"


async def main():
    c = coro1()
    r = await c
    return c, r


async def main2():
    res = []
    r1 = coro1()
    r2 = coro2()
    res.append(r1)
    res.append(r2)
    return await asyncio.gather(*res)


if __name__ == "__main__":
    # асинхронна одна функція
    start = time()
    r = asyncio.run(main())
    print(r)
    print(f"Time - {time() - start}")
    # асинхронна дві фінкції
    start = time()
    r2 = asyncio.run(main2())
    print(r2)
    print(f"Time - {time() - start}")
