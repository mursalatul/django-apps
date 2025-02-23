from django.contrib import admin
from main.models import AllApps

# Register your models here.
class AllAppsAdmin(admin.ModelAdmin):
    list_display = ['app_name']

admin.site.register(AllApps, AllAppsAdmin)
