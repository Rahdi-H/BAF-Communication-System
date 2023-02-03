from django.contrib import admin
from .models import LOS
from import_export import resources

# Register your models here.

class LOSResouce(resources.ModelResource):
    class Meta:
        model = LOS
        fields = ('serial', 'ref', 'originator', 'sender', 'receiver_unit','main_receiver', 'date_of_rec', 'time_of_rec', 'datetime_of_action', 'action_taken_by', 'file')
        export_order = ('serial', 'ref', 'originator', 'sender', 'receiver_unit','main_receiver', 'date_of_rec', 'time_of_rec', 'datetime_of_action', 'action_taken_by', 'file')

@admin.register(LOS)
class LOSAdmin(admin.ModelAdmin):
    list_display = ['serial', 'ref', 'originator', 'sender', 'written_by','main_receiver', 'date_of_rec', 'time_of_rec', 'datetime_of_action', 'action_taken_by', 'file']