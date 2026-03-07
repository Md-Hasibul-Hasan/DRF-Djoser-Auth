
from django.contrib import admin
from django.urls import path,include,re_path

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    # re_path(r'^auth/', include('djoser.social.urls')),
] 