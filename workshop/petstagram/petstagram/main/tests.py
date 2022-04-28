from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from datetime import date

from petstagram.auth_app.models import Profile

UserModel = get_user_model()


class ProfileDetailsViewTests(TestCase):
    VALID_USER_CREDENTIALS = {
        'username': 'testuser',
        'password': '12345qwe'
    }
    VALID_PROFILE_DATA = {
        'first_name': 'TEST'
        , 'last_name': 'USER'
        , 'picture': 'http://testpicture.com/url.png'
        , 'date_of_birth': date(1990, 4, 13),
    }

    @classmethod
    def __create_valid_user_and_profile(self):
        user = UserModel.objects.create_user(**self.VALID_USER_CREDENTIALS)
        profile = Profile.objects.create(
            **self.VALID_PROFILE_DATA,
            user=user,
        )
        return (user, profile)

    def test__when_opening_non_existing_profile_expect_404(self):
        pass

    def test__when_all_valid_expect_correct_template(self):
        user, profile = self.__create_valid_user_and_profile()
        response = self.client.get(reverse('auth:profile', kwargs={'pk': profile.pk}))
        self.assertTemplateUsed('accounts/profile_details.html')

    def test_when_owner__is_owner__should_be_true(self):
        response = self.client.get(reverse('auth:profile', kwargs={'pk': 1}))
        self.assertEqual(404, response.status_code)

    def test_when_user_is_owner__expect_is_owner_to_be_true(self):
        user, profile = self.__create_valid_user_and_profile()
        self.client.login(**self.VALID_USER_CREDENTIALS)
        response = self.client.get(reverse('auth:profile', kwargs={'pk': profile.pk}))
        self.assertTrue(response.context['is_owner'])

        def test_when_no_likes__should_no_likes(self):
            pass

        def test_when_no_photos__no_photos_count(self):
            pass

        def test_when_pets__should_return_owners_pets(self):
            pass

        def test_when_no_pets__pets_should_be_empty(self):
            pass

        def test_when_no_pets__likes_and_photos_count_should_be_zero(self):
            pass
