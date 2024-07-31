import asyncio
import csv
import json

import motor.motor_asyncio


async def main():
    mongo_client = motor.motor_asyncio.AsyncIOMotorClient(
        "mongodb://mongoadmin:GhjcnjGfhjkm12@localhost:27017"
    )
    db = mongo_client["test_database"]
    products = db["products"]

    # импорт продуктов из файла csv
    with open("products.csv", "r") as file:
        csv_data = csv.reader(file)
        next(file)
        for product_id, product_name in csv_data:
            await products.insert_one({"_id": int(product_id), "product_name": product_name})

    # импорт продаж из файла json
    with open("sales.json", "r") as file:
        sales_data = json.load(file)

    sales = db["sales"]
    for elem in sales_data:
        await sales.insert_one(
            {
                "_id": elem["sale_id"],
                "product_id": int(elem["product_id"]),
                "amount": elem["amount"]
            }
        )

    cursor = db.sales.aggregate(
        [
            {
                "$lookup": {
                    "from": "products",
                    "localField": "product_id",
                    "foreignField": "_id",
                    "as": "result"
                }
            },
            {"$unwind": "$result"},
            {"$project": {
                "_id": 1,
                "product_id": 1,
                "product_name": "$result.product_name",
                "amount": 1
            }}
        ]
    )

    results = await cursor.to_list(None)
    [print(el) for el in results]


asyncio.run(main())
