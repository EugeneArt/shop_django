from django.views.generic.edit import FormView

from .forms import UserForm

class RegistrationView(FormView):
    template_name = 'registration.html'
    form_class = UserForm
    success_url = '/'

    def form_valid(self, form):

        return super(RegistrationView, self).form_valid(form)