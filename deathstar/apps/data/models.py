#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models

class SensorData(models.Model):

    @staticmethod
    def get_latest_data():
        return [
            {'x':5135,'y':5042,'z':5000},
            {'x':5125,'y':5079,'z':5000},
            {'x':5121,'y':5113,'z':5000},
            {'x':5120,'y':5146,'z':5000},
            {'x':5122,'y':5178,'z':5000},
            {'x':5128,'y':5211,'z':5000},
            {'x':5136,'y':5245,'z':5000},
            {'x':5147,'y':5281,'z':5000},
            {'x':5161,'y':5319,'z':5001},
            {'x':5176,'y':5361,'z':5001},
        ]
