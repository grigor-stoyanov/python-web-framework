from django.urls import path
from django.views.generic import RedirectView

from petstagram.auth_app.views.auth import UserLoginView, UserRegisterView, ProfileDetailsView, EditProfileView, \
    ChangeUserPasswordView

app_name = 'auth'
urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login user'),
    path('<int:pk>/', ProfileDetailsView.as_view(), name='profile'),
    path('register/', UserRegisterView.as_view(), name='create profile'),
    path('edit/<int:pk>/', EditProfileView.as_view(), name='edit profile'),
    path('edit-password/', ChangeUserPasswordView.as_view(success_url='auth:password_change_done'),
         name='change password'),
    # path('edit-password/',ChangeUserPasswordView.as_view(),name='change password'),
    # path('password_change_done/',RedirectView.as_view(url='dashboard'))
]
