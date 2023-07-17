import aiomysql
import asyncio


async def execute(host: str, username: str, password: str, db: str):
    print("开始执行: ", host)

    # 网络IO：创建mysql链接，同时也会切换到其他任务执行
    conn = await aiomysql.connect(host=host, port=3306, user=username, password=password, dp=db)

    # 网络IO：创建cursor，同时也会切换到其他任务执行
    cur = await conn.cursor()

    # 网络IO：执行SQL，同时也会切换到其他任务执行
    await cur.execute("select Host, User from user")

    # 网络IO：获取SQL结果，同时也会切换到其他任务执行
    result = await cur.fetchall()
    print(result)

    # 网络IO：关闭链接，同时也会切换到其他任务执行
    await cur.close()
    await conn.close()


if __name__ == "__main__":
    tasks = [
        execute("address1", "username1", "pwd1", "mysql1"),
        execute("address2", "username2", "pwd2", "mysql2")
    ]
    asyncio.run(asyncio.wait(tasks))
