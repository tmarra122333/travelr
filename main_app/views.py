from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Profile, City, Guide
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.base import TemplateView, View
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import UserProfileForm
from django.urls import reverse

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
class ProfilePage(DetailView):
    model = Profile
    template_name = "profile.html"


class CityCreate(CreateView):
    model = City
    template_name = "city_create.html"
    fields = ['name', 'image', 'country', 'grid_img']
    
    #TODO: Change this to bring you to the city detail view when its done
    def get_success_url(self):
        return reverse('starter')


class ProfileUpdate(UpdateView):
    model = Profile
    fields = ['first_name', 'last_name', 'city', 'profile_pic', ]
    template_name = "profile_update.html"
    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.object.pk})