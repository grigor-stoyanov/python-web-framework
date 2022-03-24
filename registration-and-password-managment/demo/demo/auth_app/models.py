from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models
from demo.auth_app.managers import AppUsersManager

''''
1. Create a model extending AbstractBaseUser and PermissionsMixin
2. Tell Django for your user model AUTH_USER_MODEL in settings
3. Create user manager manager (manage.py createsuperuser ect.)
Does not have relations!
We need to make it as first migration!
'''


class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    # AbstractBaseUser gives us only password,last_login,save_method,__str__username,password_validation and other
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False
    )
    # we need to set the username used for authentication combination
    USERNAME_FIELD = 'email'
    # permissions mixin gives us superuser,groups,user_permissions,get_user_perms and ect.
    is_staff = models.BooleanField(
        default=False,
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
    )
    objects = AppUsersManager()


# now we create profile with additional data
# this is optimal because we make fewer changes when we improve authentication
class Profile(models.Model):
    first_name = models.CharField(
        max_length=25,
    )
    # now every user/profile will have the same primary key
    user = models.OneToOneField(AppUser, on_delete=models.CASCADE, primary_key=True)
