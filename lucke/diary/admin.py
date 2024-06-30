from django.contrib import admin
from .models import Diary
from django.contrib.auth import get_user_model

# Register your models here.

CustomUser = get_user_model()

@admin.register(Diary)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at', 'author')
