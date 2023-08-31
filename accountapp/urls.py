from django.urls import path

from accountapp.views import hello_world,tt

urlpatterns = [
    path('hello_world/', hello_world),
]