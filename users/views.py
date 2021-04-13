from django.urls import reverse_lazy
from django.views.generic import CreateView
from.form import UserCreationForm

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')
