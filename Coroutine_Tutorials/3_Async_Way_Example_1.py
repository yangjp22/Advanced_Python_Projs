import requests
import aiohttp
import asyncio
import time


# 普通方式下载
def download_image(url):
    print("开始下载")
    response = requests.get(url)
    print("下载完成")

    file_name = url.rsplit("_")[-1]
    with open("./files/" + file_name, "wb") as fp:
        fp.write(response.content)


# 协程方式
async def fetch(session, url):
    print("发送请求: ", url)
    async with session.get(url, verify_ssl=False) as response:
        content = await response.content.read()
        file_name = url.rsplit("_")[-1]
        with open("./files/" + file_name, "wb") as fp:
            fp.write(content)


async def main():
    async with aiohttp.ClientSession() as session:
        url_list = [
            "https://www.seiu1000.org/sites/main/files/main-images/camera_lense_0.jpeg",
            "https://static4.depositphotos.com/1003326/319/i/450/depositphotos_3191160-stock-photo-blurry-bright-background.jpg",
            "https://dfstudio-d420.kxcdn.com/wordpress/wp-content/uploads/2019/06/digital_camera_photo-1080x675.jpg"]
        tasks = [asyncio.create_task(fetch(session, url)) for url in url_list]
        await asyncio.wait(tasks)


async def download_image2(url):
    print("开始下载: ", url)

    loop = asyncio.get_running_loop()
    future = loop.run_in_executor(None, requests.get, url)
    response = await future
    file_name = url.rsplit("_")[-1]
    with open("./files/" + file_name, "wb") as fp:
        fp.write(response.content)


if __name__ == "__main__":
    url_lists = [
        "https://www.seiu1000.org/sites/main/files/main-images/camera_lense_0.jpeg",
        "https://static4.depositphotos.com/1003326/319/i/450/depositphotos_3191160-stock-photo-blurry-bright-background.jpg",
        "https://dfstudio-d420.kxcdn.com/wordpress/wp-content/uploads/2019/06/digital_camera_photo-1080x675.jpg"]
    start = time.time()
    for item in url_lists:
        download_image(item)
    print("Time used: ", time.time() - start)

    start_2 = time.time()
    tasks = [download_image2(url) for url in url_lists]
    asyncio.run(asyncio.wait(tasks))

    print("Time used: ", time.time() - start_2)
