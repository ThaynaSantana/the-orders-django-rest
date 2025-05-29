import logging
import time

from django_rq import job

from core.exceptions import ServiceUnavailabreException

logger = logging.getLogger(__name__)


@job
def example_task(param):
    """
    exemplo de task assincrona
    """
    logger.info(f"Iniciando tarefa com parametro: {param}")
    time.sleep(5)
    logger.info(f"Tarefa concluida com parametro: {param}")
    return f"Tarefa processada com {param}"


@job
def risky_task():
    raise ServiceUnavailabreException("Falha simulada")
