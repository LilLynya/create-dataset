from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.contrib.auth.views import LoginView

# Forms
from .forms import AuthForm, RegisterForm


# Create your views here.
class AuthView(LoginView):
    form_class = AuthForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('workspace:workspace')


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        extra_context = {
            'form': form,
        }
        return render(request, 'signup.html', context=extra_context)

    def post(self, request):
        form = RegisterForm(request.POST)
        extra_context = {
            'form': form
        }
        if form.is_valid():
            new_account = form.save(commit=False)
            new_account.set_password(form.cleaned_data['password'])
            new_account.save()
            return HttpResponseRedirect(reverse('workspace:workspace'))
        return render(request, 'signup.html', context=extra_context)