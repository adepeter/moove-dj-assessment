from django.contrib.auth import get_user_model
from django.urls import reverse, path, include

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, URLPatternsTestCase

from ...models import Applicant

User = get_user_model()


class ApplicantAPITest(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('applicants/', include('Moove_Assessment_Api.urls.applicant', namespace='applicant')),
    ]

    def setUp(self):
        self.data = {
            'email': 'adepeter26@gmail.com',
            'first_name': 'Peter',
            'last_name': 'Aderibigbe',
            'age': 50,
            'country': 'Nigeria',
            'address': 'Yobe State Specialist Hospital Potiskum',
            'is_hired': False
        }
        self.applicant_adepeter = Applicant.objects.create(**self.data)
        self.user = User.objects.create(username='test', password='test', email='test@test.com')
        self.token, _ = Token.objects.get_or_create(user=self.user)

    def test_baddata_responses(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        create_url = reverse('applicant:applicant_create')
        applicant_create_response = self.client.post(create_url, data={}, format='json')
        self.assertEqual(applicant_create_response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_applicant_retrieve_endpoint(self):
        kwargs = {
            'pk': self.applicant_adepeter.id
        }
        retrieve_applicant_endpoint = reverse('applicant:applicant_retrieve', kwargs=kwargs)
        applicant_retrieve_response = self.client.get(retrieve_applicant_endpoint, format='json')
        self.assertEqual(applicant_retrieve_response.status_code, status.HTTP_200_OK)

    def test_applicants_list_endpoint(self):
        list_applicants_endpoint = reverse('applicant:applicants_list')
        applicants_list_response = self.client.get(list_applicants_endpoint, format='json')
        self.assertEqual(applicants_list_response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(applicants_list_response.data), 1)
