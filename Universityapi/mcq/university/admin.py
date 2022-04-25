from django.contrib import admin
from .models import *
from django.utils import timezone
import time
ts = time.time()

class UniversityAdmin(admin.ModelAdmin):
    list_display = ['university_name','university_city','created_at','updated_at','created_by','updated_by']
    
    fieldsets = [
        (None, { 'fields': [('university_name','university_city')] } )]

    def save_model(self, request, obj, form, change):
        
        
        if getattr(obj, 'created_by', None) is None:
            obj.created_by = request.user
            obj.created_at = int(ts)
        obj.updated_by = request.user
        obj.updated_at = int(ts)
        obj.save()

admin.site.register(University,UniversityAdmin)

class UniversityContactAdmin(admin.ModelAdmin):
    list_display = ['contact_name','contact_number','contact_email','university_id','contact_type','updated_at','created_by','updated_by']
    readonly_fields = ['created_by','updated_by','created_at','updated_at']

    def save_model(self, request, obj, form, change):
        
        if getattr(obj, 'created_by', None) is None:
            obj.created_by = request.user
            obj.created_at = int(ts)
        obj.updated_by = request.user
        obj.updated_at = int(ts)
        obj.save()

admin.site.register(UniversityContacts2,UniversityContactAdmin)