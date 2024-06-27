from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('<int:pk>/', views.blog_detail, name='blog_detail'),
    path('new/', views.blog_new, name='blog_new'),
    path('<int:pk>/edit/', views.blog_edit, name='blog_edit'),
    path('<int:pk>/delete/', views.blog_delete, name='blog_delete'),
]