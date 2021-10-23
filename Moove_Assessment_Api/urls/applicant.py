from django.urls import path, include

from ..apiviews.applicant import (
    ApplicantsListAPIView,
    ApplicantCreateAPIView,
    ApplicantUpdateAPIView,
    ApplicantDeleteAPIView,
    ApplicantRetrieveAPIView
)

app_name = 'applicant'

urlpatterns = [
    path('', include([
        path('', ApplicantsListAPIView.as_view(), name='applicants_list'),
        path('create/', ApplicantCreateAPIView.as_view(), name='applicant_create'),
        path('<int:pk>/', include([
            path('', ApplicantRetrieveAPIView.as_view(), name='applicant_retrieve'),
            path('update/', ApplicantUpdateAPIView.as_view(), name='applicant_update'),
            path('delete/', ApplicantDeleteAPIView.as_view(), name='applicant_delete'),
        ])),
    ]))
]
