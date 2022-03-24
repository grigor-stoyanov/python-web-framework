import datetime

from django.contrib.auth import get_user_model
from django.db import models

from petstagram.common.validators import file_max_size, MinDateValidator

UserModel = get_user_model()


# Create your models here.

class Pet(models.Model):
    # Constants
    NAME_MAX_LENGTH = 30
    CAT = 'Cat'
    DOG = 'Dog'
    BUNNY = 'Bunny'
    PARROT = 'Parrot'
    FISH = 'Fish'
    OTHER = 'Other'
    MIN_DATE = datetime.date(1920, 1, 1)
    TYPES = [(x, x) for x in (CAT, DOG, BUNNY, PARROT, FISH, OTHER)]
    # fields
    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        unique=True,
    )
    type = models.CharField(
        choices=TYPES,
        max_length=max(len(x) for (x, _) in TYPES)
    )
    birth_date = models.DateField(
        null=True,
        blank=True,
        validators=(
            MinDateValidator(MIN_DATE),
        )
    )
    # relations one-to-one,one-to-many,many-to-many
    # one to many one user can have many pets but every pet 1 user
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    @property
    def age(self):
        return datetime.datetime.now().year - self.birth_date.year

    class Meta:
        # makes a unique pairing u can have multiple same pet names
        # with different owners but 1 owner has unique pets
        unique_together = ('user', 'name')


class PetPhoto(models.Model):
    photo = models.ImageField(
        validators=(
            file_max_size,
        )
    )
    # TODO validate at least 1 pet
    tagged_pets = models.ManyToManyField(
        Pet,
        null=False,
    )
    user = models.ForeignKey(UserModel,
                             on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    publication_date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
