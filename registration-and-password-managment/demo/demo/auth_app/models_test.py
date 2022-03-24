from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


# extending django user in out application
# v1 Model inheritance without new table proxy-model extend behaviour
# cannot add fields to AbstractUser class but can add methods
class UserWithFullNameProxy(UserModel):
    class Meta:
        # this line wont create table in database
        proxy = True
        ordering = ('first_name',)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


# v2 Creating our Own Model table with one-to-one relationship User with Profile
# user model stays clean and only cares about authentication
class Profile(models.Model):
    # fields
    # profile image
    # date of birth
    # pets
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)


# v3 extend AbstractBaseUser with more fields Only User Model
class CustomUser:
    # fields
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)


# v4 Almost completely custom user model
# combination version
class AppUser:
    pass
    # email
    # password
    # is_staff
    # is_superuser


class Profile2:
    # first Name
    # last name
    user = models.OneToOneField(AppUser, on_delete=models.CASCADE)
