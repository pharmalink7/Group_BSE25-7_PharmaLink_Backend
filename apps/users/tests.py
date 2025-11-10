from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from apps.pharmacies.models import Pharmacy  # ✅ new import

User = get_user_model()

class UserModelTest(TestCase):
    def setUp(self):
        # ✅ Create a sample pharmacy for user linkage
        self.pharmacy = Pharmacy.objects.create(
            name="Test Pharmacy",
            address="123 Main St"
        )

    def test_create_user(self):
        """Test creating a new user"""
        user = User.objects.create_user(
            email='test@example.com',
            password='testpass123',
            pharmacy=self.pharmacy
        )
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.check_password('testpass123'))
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertEqual(user.pharmacy, self.pharmacy)

    def test_create_superuser(self):
        """Test creating a new superuser"""
        user = User.objects.create_superuser(
            email='admin@example.com',
            password='adminpass123',
            pharmacy=self.pharmacy
        )
        self.assertEqual(user.email, 'admin@example.com')
        self.assertTrue(user.check_password('adminpass123'))
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
        self.assertEqual(user.pharmacy, self.pharmacy)

    def test_user_str_representation(self):
        """Test user string representation"""
        user = User.objects.create_user(
            email='test@example.com',
            password='testpass123',
            pharmacy=self.pharmacy
        )
        self.assertEqual(str(user), 'test@example.com')


class UserAPITest(APITestCase):
    def setUp(self):
        # ✅ Create a pharmacy for test users
        self.pharmacy = Pharmacy.objects.create(
            name="API Pharmacy",
            address="456 Test Avenue"
        )
        self.user = User.objects.create_user(
            email='test@example.com',
            password='testpass123',
            pharmacy=self.pharmacy
        )

    def test_user_creation_via_api(self):
        """Test user creation through API"""
        data = {
            'email': 'newuser@example.com',
            'password': 'newpass123',
            'pharmacy': self.pharmacy.id  # ✅ include pharmacy ID
        }
        response = self.client.post('/api/users/register/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_login_via_api(self):
        """Test user login through API"""
        data = {
            'email': 'test@example.com',
            'password': 'testpass123'
        }
        response = self.client.post('/api/token/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
