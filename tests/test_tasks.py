import pytest
from django_rq import get_queue

from tasks.services import enqueue_example_task
from tasks.tasks import example_task


@pytest.mark.django_db
def test_enqueue_task():
    job_id = enqueue_example_task("hello")
    queue = get_queue("default")
    job = queue.fetch_job(job_id)
    assert job is not None
    assert job.func_name == "tasks.tasks.example_task"


def test_example_task_execution():
    result = example_task("test")
    assert "test" in result
