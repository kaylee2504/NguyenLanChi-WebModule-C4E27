from pymongo import MongoClient
from faker import Faker
from random import randint, choice

faker = Faker()

mongo_uri = "mongodb+srv://admin:admin@c4e27-cluster-v9wvw.mongodb.net/test?retryWrites=true"

client = MongoClient(mongo_uri)

pilot_app = client.db_pilot

Services = pilot_app["services"]

# for i in range(50):
#     new_service = {
#         "name": faker.name(),
#         "age": randint(18, 30),
#         "gender": choice(["male", "female"]),
#         "height": randint(150, 190),
#         "available": choice([True, False]),
#         "address": faker.address(),
#     }

#     services.insert_one(new_service)
#     print("Saving document {0}......".format(i+1))