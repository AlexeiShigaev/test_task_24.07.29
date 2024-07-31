# test_task_24.07.29
4 задачки

## Задача 1
Cкрипт подключается к API и получает данные.<br>
Например, публичное API https://jsonplaceholder.typicode.com/posts <br> 
Сохраняем полученные данные в формате JSON в файл.<br>

Для теста ```python test1.py``` <br>
Доступно в swagger через браузер http://127.0.0.1:8000/docs#/default/query_query_get

## Задача 2


## Задача 3
Объединение данных из разных источников
Скрипт объединяет данные из двух источников.<br>
Первый источник - это CSV-файл с информацией о продуктах (поля: product_id, product_name).<br>
Второй источник - это JSON-файл с данными о продажах (поля: sale_id, product_id, amount).<br>
Скрипт объединяет данные по product_id и выводит итоговую таблицу с информацией о продажах для каждого продукта.

Организовано с использованием MongoDB, для запуска использовать docker-compose.yaml<br>
```
docker compose up --build
python test3.py
```

## Задача 4
Исходный скрипт. Задача оптимизировать.

```
numbers = [i for i in range(1, 1000001)]
squares = []
for number in numbers:
    squares.append(number ** 2)
```
    
Для теста ```python test4.py```

