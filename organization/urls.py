
from django.urls import path
from . import views

urlpatterns = [
    path('', views.organization_list, name='organization_list'),
    # path('<int:pk>/', views.organization_detail, name='organization_detail'),
    # path('new/', views.organization_new, name='organization_new'),
    # path('<int:pk>/edit/', views.organization_edit, name='organization_edit'),
    # path('<int:pk>/delete/', views.organization_delete, name='organization_delete'),
]