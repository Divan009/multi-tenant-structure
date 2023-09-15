from celery import shared_task
from .models import AdditionResult

result = 1

@shared_task
def add_numbers():
    global result
    print("Running add numbers periodic task")
    result += result
    AdditionResult.objects.create(answer=result)