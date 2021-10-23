from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView
)

from ..models import Applicant
from ..serializers.applicant import ApplicantSerializer


class APIViewMixin:
    serializer_class = ApplicantSerializer
    queryset = Applicant.objects.all()


class ApplicantsListAPIView(APIViewMixin, ListAPIView):
    pass


class ApplicantCreateAPIView(APIViewMixin, CreateAPIView):
    pass


class ApplicantRetrieveAPIView(APIViewMixin, RetrieveAPIView):
    pass


class ApplicantUpdateAPIView(APIViewMixin, UpdateAPIView):
    pass


class ApplicantDeleteAPIView(APIViewMixin, DestroyAPIView):
    pass
