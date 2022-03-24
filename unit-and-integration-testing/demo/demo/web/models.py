from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, ValidationError


def validate_only_letters(value):
    invalid_chars = [ch for ch in value if not ch.isalpha()]
    if invalid_chars:
        raise ValidationError(f'Value must contain only letters, but contains: {invalid_chars}')


class Profile(models.Model):
    # no need to test for Built-in Django Functions
    first_name = models.CharField(
        max_length=25,
        validators=(validate_only_letters,)
    )
    last_name = models.CharField(
        max_length=25,
        validators=(validate_only_letters,)
    )
    age = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(150)
        ]
    )

    # custom logic must be tested!
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
