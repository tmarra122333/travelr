from django.urls import path
from . import views 


urlpatterns = [
    path('', views.StarterView.as_view(), name="starter"),
    path('accounts/signup', views.Signup.as_view(), name = "signup"),
    path('profile/create', views.Create_Profile.as_view(), name = "create_profile"),
    path('profile/', views.Profile.as_view(), name = "profile"),
]