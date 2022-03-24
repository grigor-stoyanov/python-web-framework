# one way to test is request factory
# allows us to make a request object
# request = self.factory.get('url')
# setup the request the way we want it and call view as a function
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from demo.web.models import Profile
from demo.web.views import ProfileListView

UserModel = get_user_model()


class TestProfileListView(TestCase):

    def test_get__expect_correct_template(self):
        # receives response and view data before it reaches template
        response = self.client.get(reverse('profile list'))
        self.assertTemplateUsed(response, 'profile/list.html')

    # on every test django uses a new database
    def test_get__when_two_profiles__expect_context_to_contain_two_profiles(self):
        # Arrange
        profiles_to_create = (
            Profile(
                first_name='Doncho',
                last_name='Minkov',
                age=15
            ),
            Profile(
                first_name='Minko',
                last_name='Donchev',
                age=19
            )
        )
        Profile.objects.bulk_create(profiles_to_create)
        # Act
        response = self.client.get(reverse('profile list'))
        profiles = response.context['object_list']
        # check for actual profiles
        # Assert
        self.assertEqual(len(profiles), 2)

    def test_get__when_not_logged_in_user__expect_context_user_to_be_No_user(self):
        response = self.client.get(reverse('profile list'))
        self.assertEqual(
            ProfileListView.no_logged_in_user_value,
            response.context[ProfileListView.context_user_key]
        )

    def test_get__when_logged_in_user__expect_context_user_to_be_username(self):
        user_data = {
            'username': 'dell',
            'password': 'dell123'
        }
        UserModel.objects.create_user(**user_data)
        self.client.login(**user_data)
        response = self.client.get(reverse('profile list'))

        self.assertEqual(
            user_data['username'],
            response.context[ProfileListView.context_user_key]
        )
