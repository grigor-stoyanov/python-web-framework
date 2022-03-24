# validators must raise validation error or return none
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


def always_valid(chars):
    def validator(value):
        pass
    return validator


def only_letters_validator(value):
    if not value.isalpha():
        raise ValidationError


def file_max_size(value):
    file_size = value.file.size
    limit_mb = 5
    if file_size > limit_mb * 1024 * 1024:
        raise ValidationError("Max size of file is %s MB" % limit_mb)

@deconstructible
class MinDateValidator:
    def __init__(self,min_date):
        self.min_date = min_date

    def __call__(self, value):
        if value < self.min_date:
            raise ValidationError(f'date must be greater than {self.min_date}')

@deconstructible
class MaxDateValidator:
    def __init__(self, max_date):
        self.min_date = max_date

    def __call__(self, value):
        if value > self.max_date:
            raise ValidationError(f'date must be lesser than {self.max_date}')
