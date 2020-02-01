from django.contrib import admin

from map.models import MapMarks

class MapMarksAdmin(admin.ModelAdmin):
    list_display = ('name', 'id',)

admin.site.register(MapMarks, MapMarksAdmin)