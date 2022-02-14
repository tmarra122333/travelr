from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.base import TemplateView, View

# Create your views here.


class StarterView(TemplateView):
    template_name = 'starter.html'

class Signup(View):
    # show a form to fill out
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    # on form ssubmit validate the form and login the user.
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("starter")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)

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