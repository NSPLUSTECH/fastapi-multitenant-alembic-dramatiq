import dramatiq
import os
from dotenv import load_dotenv
from dramatiq.brokers.rabbitmq import RabbitmqBroker

load_dotenv()
def set_host():
    rabbitmq_broker = RabbitmqBroker(
        host=os.getenv("RABBITMQ_HOST"),
    )
    dramatiq.set_broker(rabbitmq_broker)

set_host()

from app.background_tasks.example_task import example_task