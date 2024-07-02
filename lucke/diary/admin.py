from django.contrib import admin
from .models import Diary, Sidenote
from django.contrib.auth import get_user_model

# Register your models here.

CustomUser = get_user_model()

class SideNoteInline(admin.TabularInline):
    model = Sidenote
    extra = 1
class DiaryAdmin(admin.ModelAdmin):
    inlines = [SideNoteInline]
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at', 'author')

admin.site.register(Diary, DiaryAdmin)
admin.site.register(Sidenote)