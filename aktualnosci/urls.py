from django.urls import path
from . import views

urlpatterns = [
    # path('', views.blog_list, name='blog_list'),
    path("<int:pk>/", views.blog_detail, name="blog_detail"),
    path("new/", views.blog_new, name="blog_new"),
    path("edit/<int:pk>/", views.blog_edit, name="blog_edit"),
    path(
        "fkp/",
        views.blog_list_fundacja_kochania_poznania,
        name="blog_list_fundacja_kochania_poznania",
    ),
    path(
        "pomniki/", views.blog_list_pomniki_poznania, name="blog_list_pomniki_poznania"
    ),
    path("ws/", views.blog_list_wspolna_sprawa, name="blog_list_wspolna_sprawa"),
    path("cieliczko/", views.blog_list_cieliczko_pl, name="blog_list_cieliczko_pl"),
    path(
        "legendy/",
        views.blog_list_poznanskie_legendy,
        name="blog_list_poznanskie_legendy",
    ),
]
