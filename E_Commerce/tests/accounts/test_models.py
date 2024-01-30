from rest_framework.test import APITestCase
from E_Commerce.accounts.models import User

class TestModel(APITestCase):
    def test_creates_user(self):
        user = User.objects.create_user(
            'praise','praise@gmail.com','password123!@'
        )
        self.assertIsInstance(user,User)
        self.assertFalse(user.is_staff)
        self.assertEqual(user.email, 'praise@gmail.com')

    def test_raises_error_with_messsage_when_no_username_is_supplied(self):
        self.assertRaises(ValueError,User.objects.create_user, username='',
                          email='praise@gmail.com', password='password123!@')
        

    def test_raises_error_with_message_when_no_username_is_supplied(self):
        with self.assertRaisesMessage(ValueError, 'The given username must be set'): User.objects.create_user(username='', email='praise@gmail.com',password='password123!@')

    
    def test_raises_error_when_no_email_is_supplied(self):
        self.assertRaises(ValueError, User.objects.create_user, username='', email='praise@gmail.com', password='password123!@')

    def test_cant_create_super_user_with_no_super_user_status(self):
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_superuser=True'):
            User.objects.create_superuser(username='username', email='praise@gmail.com',password='password123!@', is_superuser=False)

    def test_cant_create_super_user_with_no_staff_user_status(self):
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_staff=True'):
            User.objects.create_superuser(username='username',email='praise@gmail.com',password='password123!@',is_staff=False)

    def test_creates_super_user(self):
        user = User.objects.create_superuser(
            'praise','praise@gmail.com','password123!@')
        self.assertIsInstance(user,User)
        self.assertTrue(user.is_staff)
        self.assertEqual(user.email, 'praise@gmail.com')