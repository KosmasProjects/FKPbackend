from django.urls import path
from . import views

urlpatterns = [
    path('', views.person_list, name='person_list'),
    path('<int:pk>/', views.person_detail, name='person_detail'),
    path('new/', views.person_new, name='person_new'),
    path('<int:pk>/edit/', views.person_edit, name='person_edit'),
    path('<int:pk>/delete/', views.person_delete, name='person_delete'),
]