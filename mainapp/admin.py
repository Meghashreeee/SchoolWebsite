from django.contrib import admin
from .models import *

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('Name','content')
    list_filter = ('Name',)
    search_fields = ('Name',)
    ordering = ('Name',)

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('announcement','date')
    list_filter = ('date',)
    search_fields = ('announcement',)
    ordering = ('date',)

@admin.register(faculty)
class facultyAdmin(admin.ModelAdmin):
    list_display = ('name','position')
    list_filter = ('name',)
    search_fields = ('name','position')
    ordering = ('name',)

@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
