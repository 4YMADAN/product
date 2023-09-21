from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("lessons/", include("lessons.urls")),
    path('admin/', admin.site.urls),
]
