from django.urls import path
from . import views 


urlpatterns = [
    path('', views.StarterView.as_view(), name="starter"),
    path('about/', views.About.as_view(), name="about"),
    path('accounts/signup', views.Signup.as_view(), name = "signup"),
    path('profile/create', views.Create_Profile.as_view(), name = "create_profile"),
    path('profile/', views.Profile.as_view(), name = "profile"),
    path('city/add', views.CityCreate.as_view(), name = "city_create")
]