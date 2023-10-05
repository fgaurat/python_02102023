import requests
from bs4 import BeautifulSoup
from pprint import pprint
import time
import threading


def download_and_write(url):
    file_name =url.split("/")[-1] 
    response = requests.get(url)
    with open(file_name,"w") as f:
        f.write(response.text)


def main():
    start = time.perf_counter()
    url="https://logs.eolem.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    all_href = [f"{url}{a['href']}" for a in soup.find_all('a') if ".log" in a['href']]


    threads = []
    for href in all_href:
        th = threading.Thread(target=download_and_write,args=[href])
        th.start()
        threads.append(th)

    for th in threads:
        th.join()
    end = time.perf_counter()

    print("time :",end-start)

if __name__=='__main__':
    main()
