from django.urls import path
from . import views 


urlpatterns = [
    path('', views.StarterView.as_view(), name="starter"),
]