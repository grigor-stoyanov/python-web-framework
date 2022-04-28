from unittest import TestCase
# django testcase extends built in unittest
from django.test import TestCase as DTestCase
from lost_and_found.web.models import Profile


class TestProfile(TestCase):
    def test_profile_when_first_name_contains_only_letters__expect_success(self):
        pass

    def test_profile_when_first_name_contains_digits__expect_fail(self):
        pass

    def test_profile_when_name_contains_dollar_sign__expect_fail(self):
        pass

    def test_profile_create__when_first_name_contains_space__expect_fail(self):
        pass

    def test_profile_full_name__when_valid__expect_correct_full_name(self):
        profile = Profile(
            first_name='Doncho',
            last_name='Minkov',
            age=15
        )
        self.assertEqual('Doncho Minkov', profile.full_name)
