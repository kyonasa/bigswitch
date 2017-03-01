from django.core.management.base import BaseCommand,CommandError        
from django.db import models
from switch.models import Switch as switch
from switch.BCF import getcookie,getallswitch
import os
ip="10.10.10.1"
class Command(BaseCommand):
    def handle(self, *args, **options):         

        bcf_switch=getallswitch(ip,getcookie(ip))
        print (len(bcf_switch))
        for i in range(len(bcf_switch)):
            try:
                switch.objects.get(ip=bcf_switch[i]["inet-address"]["ip"])
                switch.objects.filter(ip=bcf_switch[i]["inet-address"]["ip"]).update(connected = bcf_switch[i]["connected"],
                                                                                    connected_since = bcf_switch[i]["connected-since"],
                                                                                    dpid=bcf_switch[i]["dpid"],
                                                                                    fabric_connection_state=bcf_switch[i]["fabric-connection-state"],
                                                                                    fabric_last_seen_time=bcf_switch[i]["fabric-last-seen-time"],
                                                                                    fabric_role=bcf_switch[i]["fabric-role"],
                                                                                    handshake_state=bcf_switch[i]["handshake-state"],
                                                                                    inet_port=bcf_switch[i]["inet-address"]["inet-port"],
                                                                                    ip=bcf_switch[i]["inet-address"]["ip"],
#                                                                                     lacp_interface_offset=bcf_switch[i]["lacp-interface-offset"],
#                                                                                     lacp_system_mac=bcf_switch[i]["lacp-system-mac"],
                                                                                    leaf_group=bcf_switch[i]["leaf-group"],
                                                                                    model_number_description=bcf_switch[i]["model-number-description"],
                                                                                    name=bcf_switch[i]["name"],
                                                                                    serial_number_description=bcf_switch[i]["serial-number-description"],
                                                                                    shutdown=bcf_switch[i]["shutdown"],
                                                                                    software_description= bcf_switch[i]["software-description"]
                                                                                    )
                print( "have",i)
            except:
                print( "none",i)
                switch.objects.create(  connected = bcf_switch[i]["connected"],
                                        connected_since = bcf_switch[i]["connected-since"],
                                        dpid=bcf_switch[i]["dpid"],
                                        fabric_connection_state=bcf_switch[i]["fabric-connection-state"],
                                        fabric_last_seen_time=bcf_switch[i]["fabric-last-seen-time"],
                                        fabric_role=bcf_switch[i]["fabric-role"],
                                        handshake_state=bcf_switch[i]["handshake-state"],
                                        inet_port=bcf_switch[i]["inet-address"]["inet-port"],
                                        ip=bcf_switch[i]["inet-address"]["ip"],
    #                                     lacp_interface_offset=bcf_switch[i]["lacp-interface-offset"],
    #                                     lacp_system_mac=bcf_switch[i]["lacp-system-mac"],
                                        leaf_group=bcf_switch[i]["leaf-group"],
                                        model_number_description=bcf_switch[i]["model-number-description"],
                                        name=bcf_switch[i]["name"],
                                        serial_number_description=bcf_switch[i]["serial-number-description"],
                                        shutdown=bcf_switch[i]["shutdown"],
                                        software_description= bcf_switch[i]["software-description"]
                                      )