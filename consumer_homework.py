import time
import json
from config import get_connection
import pika


def process_new_message(
    channel: pika.adapters.blocking_connection.BlockingChannel, method, properties, body
):
    time.sleep(1)
    new_dict = json.loads(body)
    channel.basic_ack(delivery_tag=method.delivery_tag)
    print(new_dict)
    print(f"Новий лог: {new_dict['event']}, user_id: {new_dict['user_id']}")


def consume_message(channel: pika.adapters.blocking_connection.BlockingChannel):
    QUEUE = "logs"
    channel.basic_consume(
        queue=QUEUE,
        on_message_callback=process_new_message,
        # auto_ack=True
    )

    channel.start_consuming()


def main():
    with get_connection() as connection:
        with connection.channel() as channel:
            consume_message(channel)


if __name__ == "__main__":
    main()
