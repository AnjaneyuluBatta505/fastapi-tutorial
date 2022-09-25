import requests
from multiprocessing import Pool
from datetime import datetime


def send_request(x):
    r = requests.get('http://localhost:8000/async_categories')
    print(f"no.{x}", r.status_code)


if __name__ == '__main__':
    start = datetime.now()
    with Pool(processes=100) as pool:
        pool.map(send_request, range(500))
    end = datetime.now()
    print("time HH:MM:SS.ms", end - start)
