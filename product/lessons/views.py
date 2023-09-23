from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from django.views.generic.edit import CreateView

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'lessons/signup.html'


def index(request):
    return render(request, "lessons/index.html")
def product(request):
    return render(request, "lessons/about.html")

def registration(request):
    return render(request, "lessons/registration.html")