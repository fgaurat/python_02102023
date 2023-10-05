import httpx
import requests
from bs4 import BeautifulSoup
from pprint import pprint
import time
import asyncio


async def download_and_write_requests(url):
    file_name =url.split("/")[-1]
    loop = asyncio.get_event_loop()

    response =await loop.run_in_executor(None, requests.get, url)

    with open(file_name,"w") as f:
        f.write(response.text)

async def download_and_write(url):
    file_name =url.split("/")[-1]

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        with open(file_name,"w") as f:
            f.write(response.text)



async def main():
    start = time.perf_counter()
    url="https://logs.eolem.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    all_href = [f"{url}{a['href']}" for a in soup.find_all('a') if ".log" in a['href']]

    all_r = [download_and_write(href) for href in all_href]
    r  = await asyncio.gather(*all_r)

    end = time.perf_counter()

    print("time :",end-start)

if __name__=='__main__':
    asyncio.run(main())
