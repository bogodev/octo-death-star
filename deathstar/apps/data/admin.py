from django.contrib import admin
from django.contrib.auth.models import User
from apps.data.models import SensorData

admin.site.register(SensorData)
