import pika, os
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=os.environ.get("RABBITMQ_HOST"))
)
channel = connection.channel()

channel.queue_declare(queue="urls")


def callback(ch, method, properties, body):
    print(f"Raspando o conteúdo da URL = https://www.tecmundo.com.br/{body.decode('utf-8')}")
    time.sleep(3)
    print("[x] Conteúdo Raspado com Sucesso")


channel.basic_consume(
    queue="urls", on_message_callback=callback, auto_ack=True
)

print(" [*] Waiting for messages. To exit press CTRL+C")
channel.start_consuming()
