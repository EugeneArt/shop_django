from django.views.generic.edit import FormView
from  django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login

from .forms import SignUpForm

class SignUpView(FormView):
    template_name = 'signup.html'
    form_class = SignUpForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        if ( form.cleaned_data.get('signin') ):
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            new_user = authenticate(username=username, password=password)
            login(self.request, new_user)

        return super(SignUpView, self).form_valid(form)

class SignInView(LoginView):
    template_name = 'signin.html'

class SignOutView(LogoutView):
    pass
