from django.urls import path
from . import views

urlpatterns = [
    path('', views.partner_list, name='partner_list'),
    # path('<int:pk>/', views.partner_detail, name='partner_detail'),
    # path('new/', views.partner_new, name='partner_new'),
    # path('<int:pk>/edit/', views.partner_edit, name='partner_edit'),
    # path('<int:pk>/delete/', views.partner_delete, name='partner_delete'),
]