from django.shortcuts import render
from .models import Profile
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.base import TemplateView

# Create your views here.

class Profile(TemplateView):
    template_name = "profile.html"
    def get_context_data(self, **kwargs): #needs to be written as get_context_data
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["profile"] = Profile.objects.filter(
                name__icontains=name, user=self.request.user)
        else:
            context["profile"] = Profile.objects.filter(user=self.request.user)
        return context