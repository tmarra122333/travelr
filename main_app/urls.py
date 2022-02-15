from django.urls import path
from . import views



urlpatterns = [
    path('', views.StarterView.as_view(), name="starter"),
    path('about/', views.About.as_view(), name="about"),
    path('accounts/signup', views.Signup.as_view(), name = "signup"),
    path('<int:pk>/profile/', views.ProfilePage.as_view(), name = "profile"),
    path('<int:pk>/profile_update/', views.ProfileUpdate.as_view(), name ="profile_update"),
    path('city/add', views.CityCreate.as_view(), name = "city_create"),
    path('city/guides/add', views.GuideCreate.as_view(), name="guide_create"),
    path('<int:pk>/guides/', views.GuideDetail.as_view(), name="guide_detail")
]