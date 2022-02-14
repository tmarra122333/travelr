from django.urls import path
from . import views 


urlpatterns = [
    path('', views.StarterView.as_view(), name="starter"),
    path('accounts/signup', views.Signup.as_view(), name = "signup")
]