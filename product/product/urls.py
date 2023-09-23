from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("lessons.urls")),
    path('users/', include('lessons.urls')),
    path('users/', include('django.contrib.auth.urls')),


]
