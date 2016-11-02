"""
Definition of urls for DjangoWebProject4.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',app.views.list_tasks),
    url(r'^list_tasks$',app.views.list_tasks),
    url(r'^add_task$', app.views.add_task),
    url(r'^update_task$', app.views.update_task)
]
