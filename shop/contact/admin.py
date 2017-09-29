from django.contrib import admin

from.models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['contact_name', 'contact_email', 'contact_phone','message']
