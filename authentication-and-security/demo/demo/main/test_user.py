from django.contrib.auth import get_user_model

# incorrect way to get user model
from django.contrib.auth.models import User

# correct way to get the user model
UserModel = get_user_model()
print(UserModel == User)
doncho = UserModel(username='doncho')
# django saves password in hash
doncho.set_password('123')
print(doncho.password)
# there is always a user object if none is logged its anonymous
# creating a new user
UserModel.create_user(
    username='doncho1',
    password='12345qwe'
)
# the request keeps the logged in user in its session request.is_authenticated
# use login to login from a view