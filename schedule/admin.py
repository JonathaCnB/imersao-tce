from django.contrib import admin

from .models import Review, Schedule


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    model = Schedule
    list_display = [
        "id",
        "service",
        "get_responsible",
        "user",
        "date",
        "hour",
        "is_active",
    ]
    list_editable = ["date", "hour"]
    search_fields = ["service"]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = [
        "id",
        "schedule",
        "user",
        "rating",
        "comment",
        "created_at",
    ]
    list_display_links = ["schedule"]
    search_fields = ["service"]
