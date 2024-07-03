from django.contrib import admin
from .models import Organization


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Add 'id' to the list_display

admin.site.register(Organization, OrganizationAdmin)

