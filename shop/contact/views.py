from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import ContactForm

class ContactView(FormView):
    template_name = 'contact/contact-form.html'
    form_class = ContactForm
    success_url = '/contact/success-contact/'

    def form_valid(self, form):
        form.save()
        return super(ContactView, self).form_valid(form)
