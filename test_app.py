from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_cpu_task():
    response = client.get("/cpu-task?n=1000")
    assert response.status_code == 200
    data = response.json()
    assert data["task"] == "cpu"
    assert data["input"] == 1000
    assert isinstance(data["result_length"], int)
    assert data["result_length"] > 100


def test_io_sync_task():
    response = client.get("/io-sync-task")
    assert response.status_code == 200
    data = response.json()
    assert data["task"] == "io-sync"
    assert "data" in data
    assert "id" in data["data"]


def test_io_async_task():
    response = client.get("/io-async-task")
    assert response.status_code == 200
    data = response.json()
    assert data["task"] == "io-async"
    assert "data" in data
    assert "id" in data["data"]


def test_cpu_threadpool_task():
    response = client.get("/cpu-threadpool-task?n=1000")
    assert response.status_code == 200
    data = response.json()
    assert data["task"] == "cpu-threadpool"
    assert data["input"] == 1000
    assert isinstance(data["result_length"], int)
    assert data["result_length"] > 100


def test_cpu_processpool_task():
    response = client.get("/cpu-processpool-task?n=1000")
    assert response.status_code == 200
    data = response.json()
    assert data["task"] == "cpu-processpool"
    assert data["input"] == 1000
    assert isinstance(data["result_length"], int)
    assert data["result_length"] > 100

