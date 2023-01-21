from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, ProfileUpdateForm
from .models import Customer


class SigUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

class ProfileListView(DetailView):
    model = Customer
    template_name = "profiles/profile_list.html"

    

class UpdateProfileView(UpdateView):
    form_class = ProfileUpdateForm
    model=Customer
    template_name = "profiles/profiles_update.html"

  

    