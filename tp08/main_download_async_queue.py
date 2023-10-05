import httpx
from bs4 import BeautifulSoup
from pprint import pprint
import time
import asyncio

# def download_and_write(url):
#     file_name =url.split("/")[-1] 
#     response = requests.get(url)
#     with open(file_name,"w") as f:
#         f.write(response.text)


async def download(download_queue:asyncio.Queue,save_queue:asyncio.Queue):
    while True:
        url = await download_queue.get()
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            file_name =url.split("/")[-1]
            to_save = {
                "file_name":file_name,
                "data":response.text
            }
            save_queue.put_nowait(to_save)
        
        download_queue.task_done()

async def save(save_queue:asyncio.Queue):
    while True:
        data = await save_queue.get()
        with open(data['file_name'],"w") as f:
            f.write(data['data'])        
        save_queue.task_done()



async def main():
    start = time.perf_counter()
    url="https://logs.eolem.com/"
    download_queue = asyncio.Queue()
    save_queue = asyncio.Queue()
    
    nb_workers_download = 10
    nb_workers_save = 10
    download_tasks=[]
    save_tasks=[]
    
    for i in range(nb_workers_download):
        task = asyncio.create_task(download(download_queue,save_queue))
        download_tasks.append(task)
    
    for i in range(nb_workers_save):
        task = asyncio.create_task(save(save_queue))
        save_tasks.append(task)
    
    response = httpx.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    all_href = [f"{url}{a['href']}" for a in soup.find_all('a') if ".log" in a['href']]

    for href in all_href:
        download_queue.put_nowait(href)
    
    
    await download_queue.join() 
    await save_queue.join() 

    [download_task.cancel() for download_task in download_tasks]
    [save_task.cancel() for save_task in save_tasks]
    
    end = time.perf_counter()

    print("time :",end-start)

if __name__=='__main__':
    asyncio.run(main())
