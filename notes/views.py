from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Note


def note_list(request):
    notes = (
        Note.objects.select_related("author", "status")
        .prefetch_related("categories")
        .all()
    )
    return render(request, "notes/note_list.html", {"notes": notes})


def note_detail(request, note_id):
    note = get_object_or_404(
        Note.objects.select_related("author", "status").prefetch_related("categories"),
        pk=note_id,
    )
    return render(request, "notes/note_detail.html", {"note": note})


def user_detail(request, user_id):
    user = get_object_or_404(
        User.objects.select_related("userprofile").prefetch_related("note_set__status"),
        pk=user_id,
    )
    return render(request, "notes/user_detail.html", {"user_obj": user})
