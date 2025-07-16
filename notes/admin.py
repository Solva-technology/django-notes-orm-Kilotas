from django.contrib import admin
from .models import Note, Category, Status, UserProfile


class CategoryInline(admin.TabularInline):
    model = Note.categories.through
    extra = 1


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("id", "short_text", "author", "status", "created_at")
    list_filter = ("status", "author", "categories")
    search_fields = ("text", "author__username", "status__name")
    date_hierarchy = "created_at"
    inlines = [CategoryInline]

    def short_text(self, obj):
        return obj.text[:50] + ("..." if len(obj.text) > 50 else "")

    short_text.short_description = "Text"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    search_fields = ("title",)


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "is_final")
    list_filter = ("is_final",)
    search_fields = ("name",)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "birth_date")
    search_fields = ("user__username", "user__email")
