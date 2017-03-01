#!/bin/python
from __future__ import absolute_import

import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'untitled.settings')
# Specifying the settings here means the celery command line program will know where your Django project is.
# This statement must always appear before the app instance is created, which is what we do next:
from django.conf import settings

app = Celery('untitled')

app.config_from_object('django.conf:settings')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


# With the line above Celery will automatically discover tasks in reusable apps if you define all tasks in a separate tasks.py module.
# The tasks.py should be in dir which is added to INSTALLED_APP in settings.py.
# So you do not have to manually add the individual modules to the CELERY_IMPORT in settings.py.

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))  # dumps its own request information