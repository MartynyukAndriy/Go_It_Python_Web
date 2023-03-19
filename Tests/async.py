# Task 1 Intro

import asyncio

from time import time


async def coro():
    await asyncio.sleep(1)
    return "Hello!"


async def coro2():
    await asyncio.sleep(1.2)
    return "World"


async def main():
    start = time()
    res = []
    c = coro()
    # print(c)
    # print(dir(c))
    c2 = coro2()
    res.append(c)
    res.append(c2)
    # r1 = await c
    # r2 = await c2
    # print(r1, r2)
    print(f"Time - {time() - start}")
    result = await asyncio.gather(*res)
    print(f"Time2 - {time() - start}")
    print("After")
    return res


if __name__ == "__main__":
    r = asyncio.run(main())
    print(r)

# ----------------------------------------------------

# Task 2 Gather

# import asyncio
# from time import time, sleep

# from faker import Faker


# fake = Faker("uk-UA")


# def get_user_from_db(uuid: int):
#     sleep(0.5)
#     return {"id": uuid, "name": fake.name(), "email": fake.email()}


# async def get_user_from_db_async(uuid: int):
#     await asyncio.sleep(0.5)
#     return {"id": uuid, "name": fake.name(), "email": fake.email()}


# async def main():
#     users = []
#     for i in range(1, 4):
#         users.append(get_user_from_db_async(i))
#     return await asyncio.gather(*users)


# if __name__ == "__main__":
#     start = time()
#     for i in range(1, 4):
#         user = get_user_from_db(i)
#         print(user)
#     print(time() - start)

#     res = asyncio.run(main())
#     print(res)

# # ------------------------------------------------
# # Task 3 Create Task

# import asyncio
# from time import time, sleep

# from faker import Faker


# fake = Faker("uk-UA")


# async def get_user_from_db_async(uuid: int):
#     await asyncio.sleep(0.5)
#     return {"id": uuid, "name": fake.name(), "email": fake.email()}


# async def main():
#     users = []
#     for i in range(1, 4):
#         task = asyncio.create_task(get_user_from_db_async(i))
#         users.append(task)
#     result = await asyncio.gather(*users)
#     return result


# if __name__ == "__main__":
#     start = time()
#     res = asyncio.run(main())
#     print(res)
#     print(time() - start)

# # ------------------------------------------------------------
# # Task 4 Forever Event loop

# import asyncio
# from time import time, sleep

# from faker import Faker


# fake = Faker()


# async def send(email):
#     print(f"Hello my friend {email}")


# async def worker():
#     while True:
#         await asyncio.sleep(1)
#         await send(fake.email())


# if __name__ == "__main__":
#     asyncio.run(worker())

# # ---------------------------------
# # Task 5 Future

# import asyncio
# from asyncio import Future

# from time import sleep, time

# from faker import Faker


# fake = Faker("uk-UA")


# async def async_get_user_from_db(uuid: int, future: Future):
#     await asyncio.sleep(0.5)
#     future.set_result({"id": uuid, "name": fake.name(), "email": fake.email()})


# def make_request(uuid: int) -> Future:
#     future = Future()
#     asyncio.create_task(async_get_user_from_db(uuid, future))
#     return future


# async def main():
#     f1 = make_request(1)
#     f2 = make_request(2)
#     f3 = make_request(3)
#     print(dir(f1))
#     print(f1, f2, f3)
#     print(f1.done(), f2.done(), f3.done())
#     result = await asyncio.gather(f1, f2, f3)
#     print(f1.done(), f2.done(), f3.done())
#     return result

# if __name__ == "__main__":
#     r = asyncio.run(main())
#     print(r)


# # -------------------------------------------
# # Task 6 IO bound

# import asyncio
# from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


# def io_bound_op():
#     with open(__file__, "r") as fd:
#         return fd.read(20)


# def cpu_bound_op(power: int, p: int):
#     r = [i ** power for i in range(10 ** p)]
#     return sum(r)


# async def main():
#     loop = asyncio.get_running_loop()

#     with ThreadPoolExecutor() as pool:
#         f = await loop.run_in_executor(pool, io_bound_op)
#         print(f)

#     with ProcessPoolExecutor() as pool:
#         f = await loop.run_in_executor(pool, cpu_bound_op, 2, 5)
#         print(f)


# if __name__ == "__main__":
#     asyncio.run(main())

# ------------------------------------------------------------
# Example 7 CPU Bound

# import asyncio

# from concurrent.futures import ProcessPoolExecutor

# from faker import Faker

# from time import time

# fake = Faker()


# async def send(email):
#     print(f"Hello {email}")


# async def worker():
#     while True:
#         await asyncio.sleep(1)
#         await send(fake.email())


# def cpu_bound(counter):
#     init = counter
#     while counter > 0:
#         counter -= 1
#     print(f"Complited CPU Bound {init}")
#     return init


# async def main():
#     loop = asyncio.get_running_loop()
#     task = loop.create_task(worker())

#     with ProcessPoolExecutor(6) as executor:
#         futures = [loop.run_in_executor(executor, cpu_bound, num) for num in [
#             60_000_000, 50_000_000, 80_000_000]]
#         result = await asyncio.gather(*futures)
#         task.cancel()

#         return result


# if __name__ == "__main__":
#     start = time()
#     r = asyncio.run(main())
#     print(r)
#     print(f"Time - {time() - start}")


# # ------------------------------------------------------------
# # Example 8 IO Bound

# import asyncio
# from concurrent.futures import ThreadPoolExecutor
# from time import time

# import requests


# urls = ["https://www.google.com/",
#         "https://education.nixsolutions.com/login/index.php",
#         "https://softserve.academy/?",
#         "https://school.bloqly.com/#/login"]


# def get_preview(url: str):
#     r = requests.get(url)
#     return url, r.text[:25]


# async def main():
#     loop = asyncio.get_running_loop()
#     with ThreadPoolExecutor(6) as executor:
#         futures = [loop.run_in_executor(
#             executor, get_preview, url) for url in urls]
#         r = await asyncio.gather(*futures, return_exceptions=True)
#         return r


# if __name__ == "__main__":
#     start = time()
#     result = []
#     for url in urls:
#         result.append(get_preview(url))
#     print(result)
#     print(f"Time - {time() - start}")
#     start = time()
#     r = asyncio.run(main())
#     print(r)
#     print(f"Time - {time() - start}")
