from django.contrib import admin
from django.urls import path
from apps.login.views import login, cadastro, logout

urlpatterns = [
    path('', login, name='login'),
    path('cadastro/', cadastro, name='cadastro'),
    path('logout/', logout, name='logout'),
]
