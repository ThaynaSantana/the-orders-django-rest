import django_rq

from .tasks import example_task, risky_task


def enqueue_example_task(param):
    """
    enfileira uma tarefa
    """
    queue = django_rq.get_queue("default")
    job = queue.enqueue(example_task, param)
    return job.id


def enqueue_risky_task():
    queue = django_rq.get_queue("default")
    job = queue.enqueue(risky_task)
    return job.id
