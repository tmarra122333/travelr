from django.shortcuts import render, redirect
from .models import Profile, City, Guide
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.base import TemplateView, View
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import UserProfileForm

# Create your views here.


class StarterView(TemplateView):
    template_name = 'starter.html'

class About(TemplateView):
    template_name = "about.html"

class Signup(View):
    # show a form to fill out
    def get(self, request):
        form = UserCreationForm()
        profile_form = UserProfileForm()
        context = {"form": form, "profile_form": profile_form}
        return render(request, "registration/signup.html", context)
    # on form ssubmit validate the form and login the user.
    def post(self, request):
        form = UserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            return redirect("starter")
        else:
            context = {"form": form, "profile_form": profile_form}
            return render(request, "registration/signup.html", context)

@method_decorator(login_required, name='dispatch')
class Create_Profile(CreateView):
    model = Profile
    fields = ['user','name', 'city']
    template_name = "profile_create.html"

    

@method_decorator(login_required, name='dispatch')
class Profile(DetailView):
    model = Profile
    template_name = "profile.html"
