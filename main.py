import math
import sys

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
