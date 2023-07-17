import asyncio


async def func1():
    print("hello")
    await asyncio.sleep(2)
    print("world")


async def others():
    print("start")
    await asyncio.sleep(2)
    print("end")
    return "返回值"


async def func():
    print("execute ..")
    response = await others()
    print("IO ends, ", response)


async def main():
    print("main 开始")

    task1 = asyncio.create_task(func())
    task2 = asyncio.create_task(func())

    print("main结束")

    ret1 = await task1
    ret2 = await task2

    print(ret1, ret2)


if __name__ == "__main__":
    # asyncio.run(func1())
    # asyncio.run(func())
    asyncio.run(main())
