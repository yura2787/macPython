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

# string
# r.set("myKey", "BMW")
# r.set('myKeyTTL23', 'secret dataTTL32', ex=15)
# r.set('myKeyTTL236666666666', 'secret dataTTL32', exat=datetime.datetime(year=2025, month=5, day=15, hour=3))

# lists
# r.lpush("myList", "elem1left0")
# r.rpush("myList", "elem right")
#
# r.expire("myList", 3500)

# read list
# data = r.lrange("myList", 0, -1)
# print(data)


# dicts
# r.hset("user:123456", mapping={"name": "Alise", "age": 56})
# r.hset("user:123456", mapping={"city": "Lviv"})
# r.hset("user:123456", mapping={"age": 15})
# r.expire("user:123456", 3500)
# data = r.hgetall("user:123456")
# print(data)

# get data
# data = r.get("myKey")
# print(data)


# delete data
# r.delete("blabla")

# r.incr("views", 6)
# print(r.get("views"))


# pub/sub
# r.publish("weather", "from pycharm")


# pubsub = r.pubsub()
# pubsub.subscribe("news")
# pubsub.subscribe("weather")
# for message in pubsub.listen():
#     print(message)
