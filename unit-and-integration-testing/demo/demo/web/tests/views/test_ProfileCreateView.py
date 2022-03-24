from django.test import TestCase
from django.urls import reverse

from demo.web.models import Profile


class TestProfileCreateView(TestCase):
    VALID_PROFILE_DATA = {
        'first_name': 'Doncho',
        'last_name': 'Minkov',
        'age': 17,
    }

    def test_create_profile__when_all_valid__expect_to_create(self):
        # we cant use setup if we want to use different types of data
        # but we can make into a class attribute
        profile_data = {
            'first_name': 'Doncho',
            'last_name': 'Minkov',
            'age': 17,
        }
        self.client.post(reverse('create profile'), data=profile_data)
        profile = Profile.objects.first()
        self.assertIsNotNone(profile)
        self.assertEqual(profile_data['first_name'], profile.first_name)
        self.assertEqual(profile_data['last_name'], profile.last_name)
        self.assertEqual(profile_data['age'], profile.age)
        # Test Redirects

    def test_create_profile__when_all_valid__expect_to_redirect_to_details(self):
        response = self.client.post(reverse('create profile'), data=self.VALID_PROFILE_DATA)
        profile = Profile.objects.first()
        expected_url = reverse('profile details', kwargs={'pk': profile.pk})
        self.assertRedirects(response, expected_url)
        # Test Status Code
