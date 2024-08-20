
from django.urls import path
from .views import (
    Home,
    Calculate
)

def trigger_error(request):
    division_by_zero = 1 / 0

def large_resource(request):
   time.sleep(4)
   return HttpResponse("Done!")

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('calculate', Calculate.as_view(), name='calculate'),

    #sentry test view 
    path('sentry-debug/', trigger_error),
    path('large_resource/', large_resource)
]
