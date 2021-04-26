from django.contrib import admin
from django.contrib.messages.api import add_message
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullname', 'mobile',
                    'email', 'message', 'creationDate')
    exclude = ('creationDate',)
    search_fields = ['fullname', 'mobile', 'email']


admin.site.register(Contact, ContactAdmin)
