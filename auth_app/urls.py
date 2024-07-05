from django.urls import path
from .views import login_view, list_users

urlpatterns = [
    path('login/', login_view),
    path('users/', list_users),
]