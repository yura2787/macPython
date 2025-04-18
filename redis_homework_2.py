"""Basic connection example."""

import redis

r = redis.Redis(
    host="redis-13887.crce175.eu-north-1-1.ec2.redns.redis-cloud.com",
    port=13887,
    decode_responses=True,
    username="default",
    password="mXVqbyKDa6slOBjbDqtYQn1Q8yhio7UX",
)

for i in range(10):
    r.publish("school", "hello")


pubsub = r.pubsub()
pubsub.subscribe("school")
for message in pubsub.listen():
    data = str(message.get("data"))
    if "контрольна робота" in data.lower():
        with open("school.txt", mode="a") as file:
            file.write(data + "\n")

        print(data)
