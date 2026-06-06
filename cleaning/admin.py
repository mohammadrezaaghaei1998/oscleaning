from django.contrib import admin
from .models import Contact,Appointment

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'subject', 'message')
    ordering = ('-created_at',)



@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "cleaners_count", "service", "created_at")
    search_fields = ("name", "phone", "service")
    list_filter = ("service", "cleaners_count", "created_at")
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)