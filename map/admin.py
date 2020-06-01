from django.contrib import admin

from about.models import Comment

from map.models import MapMarks


class MapMarksAdmin(admin.ModelAdmin):
    list_display = ('name', 'id',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('User_name', 'id',)

admin.site.register(MapMarks, MapMarksAdmin)
admin.site.register(Comment, CommentAdmin)