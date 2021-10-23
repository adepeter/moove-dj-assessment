from django.contrib import admin
from django.utils.translation import gettext_lazy as _


# Register your models here.
from ..models import Applicant


@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = [
        'email',
        'first_name',
        'last_name',
        'age',
        'country',
        'is_hired'
    ]
    list_filter = [
        'is_hired'
    ]
    search_fields = [
        'email',
        'first_name',
        'last_name',
        'address',
        'age'
    ]
    fieldsets = (
        (_('Basic information'), {
            'classes': ('expand',),
            'fields': (
                'email',
                'first_name',
                'last_name',
                'age',
                'is_hired',
            ),
        }),
        (_('Address information'), {
            'classes': ('expand',),
            'fields': (
                'country',
                'address',
            ),
        }),
    )


__all__ = [
    'ApplicantAdmin'
]
