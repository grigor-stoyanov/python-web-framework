from django.urls import path

from demo.main.views import SlowTaskView

urlpatterns = [
    path('<int:is_slow>/', SlowTaskView.as_view(), name='async demo')
]
