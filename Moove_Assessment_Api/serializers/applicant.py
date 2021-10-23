from rest_framework import serializers

from django.utils.translation import gettext_lazy as _

from ..models import Applicant


class ApplicantSerializer(serializers.ModelSerializer):

    def validate_is_hired(self, is_hired):
        if is_hired is None:
            raise serializers.ValidationError(_('You cannot set hired status to None or null'))
        return is_hired

    class Meta:
        model = Applicant
        fields = '__all__'
        extra_kwargs = {
            'first_name': {
                'label': _('Name'),
            },
            'last_name': {
                'label': _('Family name'),
            },
            'country': {
                'label': _('Country of Origin'),
            },
        }
