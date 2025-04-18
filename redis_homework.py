"""Basic connection example."""

import datetime
import redis

r = redis.Redis(
    host="redis-13887.crce175.eu-north-1-1.ec2.redns.redis-cloud.com",
    port=13887,
    decode_responses=True,
    username="default",
    password="mXVqbyKDa6slOBjbDqtYQn1Q8yhio7UX",
)


# r.set("myKeyCar", "BMW")
# r.set("myKeyAnimal", "Dog", ex=10000)
r.lpush("myListProducts", "Apple", "Milk", "Biscuits")
r.expire("myListProducts", 10000)
# r.hset(
#     "ingredientCake",
#     mapping={
#         "honey": 150,
#         "butter": 50,
#         "sour cream": 70,
#         "soda": 0.5,
#         "egg": 1,
#         "flour": 150,
#         "cream": 300,
#     },
# )
# r.hset("ingredientCake", mapping={"sugar": 300})
# r.hset("ingredientCake", mapping={"sugar": 500})
#
# r.delete("ingredientCake")

# pubsub = r.pubsub()
# pubsub.subscribe("school")
# for message in pubsub.listen():
#     print(message)
