from django.urls import path
from . import views

urlpatterns = [
    path("", views.note_list, name="note_list"),
    path("notes/<int:note_id>/", views.note_detail, name="note_detail"),
    path("users/<int:user_id>/", views.user_detail, name="user_detail"),
]
