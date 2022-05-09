
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('demo.main.urls')),
    path('auth/',include('demo.auth_app.urls'))
]
