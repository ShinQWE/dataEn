import random
import string
import time
import redis
import json  # Не забудьте импортировать json

# Подключение к Redis
r = redis.Redis(host='localhost', port=6379, db=0)

while True:
    # Генерация случайного сообщения
    message = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    # Преобразование сообщения в JSON
    message_data = json.dumps({'message': message})
    r.lpush('messages', message_data)  # Отправка JSON-строки в Redis
    print(f"Sent: {message}")
    time.sleep(5)  # Ждать 1 минуту