from django.core.management.base import BaseCommand,CommandError
from django.db import models
from switch.models import Switch as switch
from switch.BCF import getcookie,getallswitch
import os
ip="10.10.10.1"
class Command(BaseCommand):
