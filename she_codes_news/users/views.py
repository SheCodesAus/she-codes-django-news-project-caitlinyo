from django.shortcuts import render

# Create your views here.
from cProfile import Profile
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic

from news.forms import StoryForm
from .models import CustomUser
from .forms import CustomUserCreationForm


# view user profile
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

#importing code from news directories
from news.models import NewsStory

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

class ProfileView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'users/ProfileView.html'





    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['latest_stories'] = NewsStory.objects.all()[:4]
    #     context['all_stories'] = NewsStory.objects.all()
    #     return context

