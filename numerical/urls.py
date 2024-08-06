
from django.urls import path
from .views import (
    Home,
    Calculate
)
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('calculate', Calculate.as_view(), name='calculate'),
]
