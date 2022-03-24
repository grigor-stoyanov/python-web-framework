from django.db import models


class Profile(models.Model):
    email = models.EmailField()
    name = models.CharField(
        max_length=25,
    )

    def __str__(self):
        return f'{self.pk} {self.name} with {self.email}'
