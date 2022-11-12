from django.urls import path
from . import views

urlpatterns = [
    path("", views.song_list_create),
    path("<int:pk>/", views.song_detail_create),
    path("<int:pk>/update/", views.song_update_create),
    path("<int:pk>/delete/", views.song_destroy_view),
]