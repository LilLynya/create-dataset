from django.contrib import admin
from django.urls import path

# Views
from .views import AuthView, RegisterView

urlpatterns = [
    path('login/', AuthView.as_view(), name='login'),
    path('signup/', RegisterView.as_view(), name='signup'),
]
