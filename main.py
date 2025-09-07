import math
import sys
import concurrent.futures

import requests
import httpx
import asyncio
from fastapi import FastAPI

sys.set_int_max_str_digits(1000000)
app = FastAPI()


def factorial(n: int) -> int:
    return math.factorial(n)


# ---- CPU-bound ----
@app.get("/cpu-task")
async def cpu_task(n: int = 20000):
    result = await asyncio.to_thread(factorial, n)
    return {"task": "cpu", "input": n, "result_length": len(str(result))}


# ---- IO-bound (синхронный) ----
@app.get("/io-sync-task")
def io_sync_task():
    url = "https://jsonplaceholder.typicode.com/todos/1"
    response = requests.get(url, timeout=5)
    return {"task": "io-sync", "data": response.json()}


# ---- IO-bound (асинхронный) ----
@app.get("/io-async-task")
async def io_async_task():
    url = "https://jsonplaceholder.typicode.com/todos/1"
    async with httpx.AsyncClient(timeout=5) as client:
        response = await client.get(url)
        return {"task": "io-async", "data": response.json()}


# ---- CPU-bound с concurrent.futures (ThreadPoolExecutor) ----
@app.get("/cpu-threadpool-task")
async def cpu_threadpool_task(n: int = 20000):
    def run_with_threadpool():
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(factorial, n)
            return future.result()

    result = await asyncio.to_thread(run_with_threadpool)

    return {
        "task": "cpu-threadpool",
        "input": n,
        "result_length": len(str(result))
    }


# ---- CPU-bound с concurrent.futures (ProcessPoolExecutor) ----
@app.get("/cpu-processpool-task")
async def cpu_processpool_task(n: int = 20000):
    def run_with_processpool():
        with concurrent.futures.ProcessPoolExecutor() as executor:
            future = executor.submit(factorial, n)
            return future.result()

    result = await asyncio.to_thread(run_with_processpool)

    return {
        "task": "cpu-processpool",
        "input": n,
        "result_length": len(str(result))
    }
