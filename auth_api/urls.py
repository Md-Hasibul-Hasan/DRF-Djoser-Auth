
from django.contrib import admin
from django.urls import path,include,re_path
from .views import GoogleLoginView

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/google/', GoogleLoginView.as_view(), name='google-login'),
] 