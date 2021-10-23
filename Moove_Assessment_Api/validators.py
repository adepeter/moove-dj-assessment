from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .services import get_country


def cannot_be_null(value):
    if value is None:
        raise ValidationError(_('You cannot save this as null'))


def validate_country_name(country_name):
    if get_country(country_name) is False:
        raise ValidationError(_('%(country)s is not a valid country' % {'country': country_name}))
