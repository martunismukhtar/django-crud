from django.contrib import admin

# Register your models here.
from .models import Album, Musician

class AlbumAdmin(admin.ModelAdmin):
    display_fields = [
        'name', 'release_date', 'num_stars'
    ]


admin.site.register(Musician)
admin.site.register(Album)