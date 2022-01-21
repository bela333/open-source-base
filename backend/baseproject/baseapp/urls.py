from django.urls import path
from baseapp import views

urlpatterns = [
    path('hello/', views.hello),
]