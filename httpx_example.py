# Отправка GET запроса
print("Отправка GET запроса")
import httpx
response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")
print(response.status_code)  # 200
print(response.json())       # {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}
print("-------------------------")



# Отправака POST запроса
print("Отправака POST запроса")
import httpx
data = {
    "title": "Новая задача",
    "completed": False,
    "userId": 1
}
response = httpx.post("https://jsonplaceholder.typicode.com/todos", json=data)
print(response.status_code)  # 201 (Created)
print(response.json())       # Ответ с созданной записью
print("-------------------------")


# Отправка данных в формате form-urlencoded вместо json
print("Отправка данных в формате form-urlencoded вместо json")
import httpx
data = {"username": "test_user", "password": "123456"}
response = httpx.post("https://httpbin.org/post", data=data)
print(response.status_code)
print(response.json())  # {'form': {'username': 'test_user', 'password': '123456'}, ...}
print("-------------------------")


# Передача заголовков
print("Передача заголовков")
import httpx
headers = {"Authorization": "Bearer my_secret_token"}
response = httpx.get("https://httpbin.org/get", headers=headers)
print(response.status_code)
print(response.json())  # Заголовки включены в ответ
print("-------------------------")


# Работа с параметрами запроса
print("Работа с параметрами запроса")
import httpx
params = {"userId": 1}
response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)
print(response.status_code)
print(response.url)    # https://jsonplaceholder.typicode.com/todos?userId=1
print(response.json()) # Фильтрованный список задач
print("-------------------------")


# Отправка файлов
print("Отправка файлов")
import httpx
files = {"file": ("example.txt", open("example.txt", "rb"))}
response = httpx.post("https://httpbin.org/post", files=files)
print(response.status_code)
print(response.json())  # Ответ с данными о загруженном файле
print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")


# РАБОТА С СЕССИЯМИ. Использование HTTPX Client
print("Работа с сессиями. Использование HTTPX Client")
import httpx

with httpx.Client() as client:
    response1 = client.get("https://jsonplaceholder.typicode.com/todos/1")
    response2 = client.get("https://jsonplaceholder.typicode.com/todos/2")

print(response1.json())  # Данные первой задачи
print(response2.json())  # Данные второй задачи
print("-------------------------")


# Добавление базовых заголовков в Client
print("Добавление базовых заголовков в Client")
import httpx
client = httpx.Client(headers={"Authorization": "Bearer my_secret_token"})
response = client.get("https://httpbin.org/get")
print(response.json())  # Заголовки включены в ответ
client.close()
print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

# РАБОТА С ОШИБКАМИ
# Проверка статуса ответа
print("Проверка статуса ответа")
import httpx
try:
    response = httpx.get("https://jsonplaceholder.typicode.com/invalid-url")
    response.raise_for_status()  # Вызовет исключение при 4xx/5xx
except httpx.HTTPStatusError as e:
    print(f"Ошибка запроса: {e}")
print("-------------------------")


# Обработка таймаутов
print("Обработка таймаутов")
import httpx
try:
    response = httpx.get("https://httpbin.org/delay/5", timeout=2)
except httpx.ReadTimeout:
    print("Запрос превысил лимит времени")
print("-------------------------")


