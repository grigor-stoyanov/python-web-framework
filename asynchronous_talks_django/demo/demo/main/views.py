import time

from django import views
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from demo.main.tasks import slow_task


class SlowTaskView(views.View):
    def get(self, request, is_slow):
        start = time.time()
        if is_slow:
            # synchronous will execute in 5 seconds
            slow_task(5)
        else:
            # asynchronous will execute in celery while response is returned in 0.15s
            slow_task.delay(5)
        end = time.time()
        return JsonResponse(data={
            'time_executed': end - start,
        })
