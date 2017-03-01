from django.contrib import admin

# Register your models here.
from switch.models import Switch

class swichlist(admin.ModelAdmin):
    list_display=('name','connected','dpid','fabric_connection_state','fabric_last_seen_time','fabric_role','handshake_state','ip','software_description','connected_since')
    search_fields=('name','connected_since')


admin.site.register(Switch,swichlist)