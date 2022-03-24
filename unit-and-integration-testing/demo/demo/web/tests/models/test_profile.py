from unittest import TestCase
# django testcase extends built in unittest
from django.core.exceptions import ValidationError
from django.test import TestCase as DTestCase
from demo.web.models import Profile


class TestProfile(DTestCase):
    VALID_USER_DATA = {
        'first_name': 'Doncho',
        'last_name': 'Minkov',
        'age': 15
    }

    def test_profile_create__when_first_name_contains_only_letters__expect_success(self):
        profile = Profile(**self.VALID_USER_DATA)
        profile.save()
        self.assertIsNotNone(profile.pk)

    def test_profile_create__when_first_name_contains_digits__expect_fail(self):
        first_name = 'Doncho1'
        profile = Profile(first_name=first_name,
                          last_name=self.VALID_USER_DATA['last_name'],
                          age=self.VALID_USER_DATA['age'], )
        with self.assertRaises(ValidationError) as context:
            # this is called in ModelForms implicitly
            profile.full_clean()
            profile.save()
        self.assertIsNotNone(context.exception)

    # testing models must explicit call full clean
    def test_profile_when_name_contains_dollar_sign__expect_fail(self):
        first_name = 'Doncho$'
        profile = Profile(first_name=first_name,
                          last_name=self.VALID_USER_DATA['last_name'],
                          age=self.VALID_USER_DATA['age'], )
        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()
        self.assertIsNotNone(context.exception)

    def test_profile_create__when_first_name_contains_space__expect_fail(self):
        first_name = 'Don cho1'
        profile = Profile(first_name=first_name,
                          last_name=self.VALID_USER_DATA['last_name'],
                          age=self.VALID_USER_DATA['age'], )
        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()
        self.assertIsNotNone(context.exception)

    def test_profile_full_name__when_valid__expect_correct_full_name(self):
        profile = Profile(**self.VALID_USER_DATA)
        self.assertEqual(f'{self.VALID_USER_DATA["first_name"]} {self.VALID_USER_DATA["last_name"]}', profile.full_name)
