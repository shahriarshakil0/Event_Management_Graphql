from django.contrib import admin
from .models import Location, Event, Event_member


admin.site.register(Location)
# @admin.register(Location)
# class LocationAdmin(admin.ModelAdmin):
#     list_display = ['id', '']


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']


admin.site.register(Event_member)
# @admin.register(Event_member)
# class EventMemberAdmin(admin.ModelAdmin):
#     list_display = ["id"]
