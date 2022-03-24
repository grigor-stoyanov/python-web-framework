from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.auth_app.managers import PetstagramUserManager
from petstagram.common.validators import only_letters_validator

'''
1. Create Model.
2. Configure Model in settings.py
3. Create user manager 
'''


class PetstagramUser(AbstractBaseUser, PermissionsMixin):
    USERNAME_MAX_LENGTH = 25
    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        unique=True,
    )
    date_joined = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    objects = PetstagramUserManager()


class Profile(models.Model):
    FIRST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 30

    GENDER_MALE = ('Male', 'Male')
    GENDER_FEMALE = ('Female', 'Female')
    GENDER_DO_NOT_SHOW = ('Do not show', 'Do not show')
    GENDERS = [GENDER_FEMALE, GENDER_MALE, GENDER_DO_NOT_SHOW]
    # id/pk by default
    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            only_letters_validator,
        ),
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            only_letters_validator,
        )
    )
    picture = models.URLField()
    birth_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    gender = models.CharField(
        max_length=max(len(x) for x, _ in GENDERS),
        choices=GENDERS,
        default=GENDER_DO_NOT_SHOW,
    )
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        primary_key=True
    )
