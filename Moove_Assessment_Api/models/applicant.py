from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from ..validators import validate_country_name


class Applicant(models.Model):
    email = models.EmailField(
        verbose_name=_('E-mail'),
        unique=True,
        help_text=_('E-mail address of applicant')
    )
    first_name = models.CharField(
        verbose_name=_('First Name'),
        validators=[MinLengthValidator(5)],
        max_length=50,
        help_text=_('First name of applicant')
    )
    last_name = models.CharField(
        verbose_name=_('Last Name'),
        max_length=50,
        validators=[MinLengthValidator(5)],
        help_text=_('Family or surname of applicant')
    )
    age = models.PositiveIntegerField(
        verbose_name=_('Age'),
        validators=[MinValueValidator(20), MaxValueValidator(60)],
        help_text=_('Age of applicant')
    )
    address = models.TextField(
        verbose_name=_('Address'),
        validators=[MinLengthValidator(10)],
        help_text=_('Residential or contact address')
    )
    country = models.CharField(
        verbose_name=_('Country'),
        max_length=20,
        validators=[validate_country_name, MinLengthValidator(2)],
        help_text=_('Country of origin of applicant')
    )
    is_hired = models.BooleanField(
        verbose_name=_('Hired status'),
        null=True,
        help_text=_('Is applicant already hired?')
    )

    def save(self, *args, **kwargs):
        self.country = self.country.title()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.email} - {self.first_name} {self.last_name}'
