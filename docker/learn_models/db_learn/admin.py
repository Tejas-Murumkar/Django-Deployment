from django.contrib import admin
from .models import Film

# Register your models here.

class FilmAdmin(admin.ModelAdmin):
    list_display = ["name", "release_year", "collection", "rating"]


admin.site.register(Film, FilmAdmin)