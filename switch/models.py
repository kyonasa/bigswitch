from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Switch(models.Model):
    connected = models.CharField(max_length=255,null=True)
    connected_since = models.CharField(max_length=255,null=True)
    dpid=models.CharField(max_length=255,null=True)
    fabric_connection_state=models.CharField(max_length=255,null=True)
    fabric_last_seen_time=models.CharField(max_length=255,null=True)
    fabric_role=models.CharField(max_length=255,null=True)
    handshake_state=models.CharField(max_length=255,null=True)
    inet_port=models.CharField(max_length=255,null=True)
    ip=models.CharField(max_length=255,null=True)
    lacp_interface_offset=models.CharField(max_length=255,null=True)
    lacp_system_mac=models.CharField(max_length=255,null=True)
    leaf_group=models.CharField(max_length=255,null=True)
    model_number_description=models.CharField(max_length=255,null=True)
    name=models.CharField(max_length=255,null=True)
    serial_number_description=models.CharField(max_length=255,null=True)
    shutdown=models.CharField(max_length=255,null=True)
    software_description=models.CharField(max_length=255,null=True)