import aioredis
import asyncio


async def execute(address: str, password: str):
    print("开始执行: ", address)

    # 网络IO：创建redis链接，同时也会切换到其他任务执行
    redis = await aioredis.from_url(address, password=password)

    # 网络IO：写入数据到redis中，同时也会切换到其他任务执行
    await redis.set("key", "string-value")

    # 网络IO：从redis中读取数据，同时也会切换到其他任务执行
    result = await redis.get("key")
    print(result)

    # 网络IO：关闭redis链接，同时也会切换到其他任务执行
    await redis.close()


if __name__ == "__main__":
    tasks = [
        execute("address1", "pwd1"),
        execute("address2", "pwd2")
    ]
    asyncio.run(asyncio.wait(tasks))
