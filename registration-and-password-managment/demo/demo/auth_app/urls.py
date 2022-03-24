from django.urls import path, include
from django.views.generic import TemplateView

from demo.auth_app.views import UserRegistrationView, UserLoginView, UserLogout, RestrictedView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register user'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),
    # we dont even need to use our own urls django provides us with urls
    # path('', include('django.contrib.auth.urls'))
    path('restricted/',RestrictedView.as_view(),name='restricted')

]
