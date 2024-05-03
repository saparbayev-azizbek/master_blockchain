from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static

from app1.views import Link

urlpatterns = [
    path('',Link.as_view(),name='home'),
]