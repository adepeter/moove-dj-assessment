from django.db import IntegrityError
from django.db.models import UniqueConstraint
from django.test import TestCase

from ...models import Applicant


class ApplicantModelTest(TestCase):
    def setUp(self):
        self.user_adepeter = Applicant.objects.create(
            email='adepeter26@gmail.com',
            first_name='Peter',
            last_name='Aderibigbe',
            age=50,
            country='Nigeria',
            address='Yobe State Specialist Hospital Potiskum',
            is_hired=False
        )

    def test_user_is_created(self):
        user = self.user_adepeter
        user_2 = Applicant.objects.create(
            email='test@example.com',
            first_name='Example',
            last_name='Admin',
            age=30,
            country='Algeria',
            address='Test Region Republic',
            is_hired=None
        )
        self.assertIsNone(user_2.is_hired)
        self.assertEqual(user.email, 'adepeter26@gmail.com')
        self.assertNotEqual(Applicant.objects.count(), 1)
        self.assertEqual(Applicant.objects.count(), 2)
