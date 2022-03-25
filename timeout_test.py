# -*- coding: utf8 -*-
# flake8: noqa
# @author: liuwangwang
# @email: liuwangwang@qianxin.com
import asyncio


async def test_timeout():
    await asyncio.sleep(2)


async def run():
    await asyncio.wait_for(
        test_timeout(), timeout=1
    )

if __name__ == '__main__':
    asyncio.run(run())
