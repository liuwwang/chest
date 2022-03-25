# -*- coding: utf8 -*-
# flake8: noqa
# @author: liuwangwang
# @email: liuwangwang@qianxin.com
import os
import asyncio
import logging


def init_logs():
    path = os.path.abspath(os.path.dirname(__file__))
    log_file_rule = os.path.join(path, "../logs/app.log")
    fh1 = logging.FileHandler(filename=log_file_rule, mode="a+")
    formatter = logging.Formatter(
        "[%(asctime)s] (%(filename)s:%(lineno)s): <%(levelname)s> %(message)s"
    )
    fh1.setFormatter(formatter)
    logger = logging.getLogger("ASYNC")
    logger.setLevel(logging.DEBUG)
    logger.addHandler(fh1)
    return logger


logger = init_logs()


async def task1():
    logger.info("task1")


async def task2():
    logger.debug("task2")


async def run():
    await asyncio.create_task(task1())
    await asyncio.create_task(task2())


async def gather_test():
    await asyncio.gather(task2(), task1(), task2(), task2(), task1(), task2())


async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({number}), currently i={i}...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")
    return f


async def main():
    # Schedule three calls *concurrently*:
    L = await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )
    print(L)


if __name__ == "__main__":
    # asyncio.run(run(), debug=True)
    # asyncio.run(gather_test(), debug=True)
    asyncio.run(main(), debug=True)
