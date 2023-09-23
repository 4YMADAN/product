from django.urls import path
from .views import SignUpView
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('about/', views.product, name='product'),
    path('registration/', views.registration, name='registration'),
    path('signup/', SignUpView.as_view(), name='signup')
]