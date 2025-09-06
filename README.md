# FastAPI Test Task

## 📖 Описание
Сервис на **FastAPI** с тремя эндпоинтами, которые демонстрируют разные типы задач:

1. **CPU-bound**  
   Эндпоинт `/cpu-task` — считает факториал числа `n`.  
   Чтобы не блокировать сервер, вычисления выполняются в отдельном потоке через `asyncio.to_thread`.

2. **IO-bound (синхронный)**  
   Эндпоинт `/io-sync-task` — выполняет синхронный HTTP-запрос через `requests`.

3. **IO-bound (асинхронный)**  
   Эндпоинт `/io-async-task` — выполняет асинхронный HTTP-запрос через `httpx.AsyncClient`.

---

## ⚙️ Установка и запуск (venv)

### 1. Клонирование проекта
```bash
git clone <repo-url>
cd project
```

### 2. Создание виртуального окружения
```bash
python3 -m venv venv
```

### 3. Активация окружения
- **Linux / macOS**
  ```bash
  source venv/bin/activate
  ```
- **Windows (PowerShell)**
  ```powershell
  venv\Scripts\activate
  ```

После активации в начале командной строки появится `(venv)`.

### 4. Установка зависимостей
```bash
pip install -r requirements.txt
```

Файл `requirements.txt` содержит:
```
fastapi
uvicorn
requests
httpx
pytest
```

### 5. Запуск сервера
```bash
uvicorn app:app --reload
```

- `app:app` → первый `app` это имя файла (`app.py`), второй `app` это объект FastAPI.  
- `--reload` → автообновление при изменениях в коде.  

После запуска API будет доступно:  
👉 Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
👉 ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)  

---

## 🔗 Эндпоинты

- **CPU-bound**  
  `GET /cpu-task?n=5000`  
  → возвращает количество цифр факториала числа `n`.

- **IO-bound sync**  
  `GET /io-sync-task`  
  → делает HTTP-запрос через `requests`.

- **IO-bound async**  
  `GET /io-async-task`  
  → делает асинхронный HTTP-запрос через `httpx`.

---

## 🧪 Тесты

Тесты написаны на `pytest` с использованием `TestClient`.

### Запуск тестов
```bash
pytest -v
```

Ожидаемый результат — все тесты проходят успешно ✅

---

