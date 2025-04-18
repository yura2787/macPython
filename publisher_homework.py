import pika.adapters.blocking_connection
from config import get_connection
from time import sleep
import json


def produce_logs(channel: pika.adapters.blocking_connection.BlockingChannel):
    QUEUE = "logs"
    channel.queue_declare(queue=QUEUE)

    for item in range(100):
        message = {"event": "user_registered", "user_id": item}
        channel.basic_publish(exchange="", routing_key=QUEUE, body=json.dumps(message))


def main():
    with get_connection() as connection:
        with connection.channel() as channel:
            produce_logs(channel)


if __name__ == "__main__":
    main()
