from django.urls import path, include

app_name = 'moove_assignment_api'

urlpatterns = [
    path('applicants/', include('Moove_Assessment_Api.urls.applicant', namespace='applicant')),
]
