from django import contrib
from .models import Contact
from .forms.contact_form import ContactForm


class ContactService():

    def create(form: ContactForm) -> int:
        fullname = form.cleaned_data['fullname']
        email = form.cleaned_data['email']
        mobile = form.cleaned_data['mobile']
        message = form.cleaned_data['message']
        contact = Contact(fullname=fullname, email=email,
                          mobile=mobile, message=message)
        contact.save()
        return contact.id
