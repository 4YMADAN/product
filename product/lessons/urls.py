from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('about/', views.product, name='product'),
    path('registration/', views.registration, name='registration'),
]