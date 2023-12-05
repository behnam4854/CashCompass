from django.test import TestCase
from django.contrib.auth import get_user_model

# def sampleUser(email='test@test.com',password='testpassword'):
#     return get_user_model().objects.create_user(email,password)

class UserRegistrationTest(TestCase):

    def setUp(self):
        
        self.user_data = {
            'name': 'Test User',
            'email': 'testuser@example.com',
            'password': 'TestPassword123!',
            'phone_number': '+1234567890'
        }

    def test_valid_registration(self):
        """
        Test that a user can successfully register with valid email, password, and phone number.
        """
        user = get_user_model().objects.create_user(**self.user_data)
        self.assertTrue(user.is_active)
        self.assertEqual(user.email, self.user_data['email'])
        self.assertTrue(user.check_password(self.user_data['password']))

    def test_invalid_email_format(self):
        """
        Test that registration fails for an invalid email format.
        """
        self.user_data['email'] = '123'
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, self.user_data['email'])

    def test_existing_email(self):
        """
        Test that registration fails for an email address that is already in use.
        """
        existing_user = get_user_model().objects.create_user(
            name='Existing User',
            email='existinguser@example.com',
            password='TestPassword123!',
            phone_number='+1234567891'
        )

        user_data = {
            'name': 'Test User',
            'email': existing_user.email,
            'password': 'TestPassword123!',
            'phone_number': '+1234567892'
        }

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(**user_data)

    def test_weak_password(self):
        """
        Test that registration fails for a password that is too short or weak.
        """
        weak_passwords = [
            '12345',
            'password',
            'test123'
        ]

        for weak_password in weak_passwords:
            user_data = {
                'name': 'Test User',
                'email': 'testuser@example.com',
                'password': weak_password,
                'phone_number': '+1234567893'
            }

            with self.assertRaises(ValueError):
                get_user_model().objects.create_user(**user_data)

    def test_invalid_phone_number_format(self):
        """
        Test that registration fails for an invalid phone number format.
        """
        invalid_phone_numbers = [
            '12345678',
            '+123456789',
            'abc1234567890'
        ]

        for invalid_phone_number in invalid_phone_numbers:
            user_data = {
                'name': 'Test User',
                'email': 'testuser@example.com',
                'password': 'TestPassword123!',
                'phone_number': invalid_phone_number
            }

            with self.assertRaises(ValueError):
                get_user_model().objects.create_user(**user_data)


