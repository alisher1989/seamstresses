from django.contrib import admin

from webapp.models import Seamstress, SewingMachines


class SeamstressAdmin(admin.ModelAdmin):
    model = Seamstress
    # list_display = ['name', 'phone', 'date', 'call_type', 'status']
    readonly_fields = ['total_price']


admin.site.register(Seamstress, SeamstressAdmin)
admin.site.register(SewingMachines)
