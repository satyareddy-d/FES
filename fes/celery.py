from celery import Celery
from celery.utils.log import get_task_logger

from fes.celeryconfig import broker_url


LOGGER = get_task_logger(__name__)
APP_NAME = 'FES'  # Fastest email service

app = Celery(APP_NAME, broker=broker_url)
app.config_from_object('celeryconfig')

