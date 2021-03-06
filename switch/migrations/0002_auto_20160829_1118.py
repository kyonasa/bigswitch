# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-29 03:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('switch', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='switch',
            name='type',
        ),
        migrations.AddField(
            model_name='switch',
            name='connected',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='switch',
            name='connected_since',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='switch',
            name='dpid',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='switch',
            name='fabric_connection_state',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='switch',
            name='fabric_last_seen_time',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='switch',
            name='fabric_role',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='switch',
            name='handshake_state',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='switch',
            name='inet_port',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='switch',
            name='ip',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='switch',
            name='lacp_interface_offset',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='switch',
            name='lacp_system_mac',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='switch',
            name='leaf_group',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='switch',
            name='model_number_description',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='switch',
            name='serial_number_description',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='switch',
            name='shutdown',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='switch',
            name='software_description',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='switch',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
