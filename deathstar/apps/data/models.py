#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings

class SensorData(models.Model):

    stamp = models.PositiveIntegerField()
    data_line = models.TextField(null=True)

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

    @staticmethod
    def get_live_data():
        return SensorData.parse_data_string(SensorData.get_data_string(1))

    @staticmethod
    def get_data_string(index):
        return "1;O,5135,5042,5000;M,10000,10000,10000"

    @staticmethod
    def import_test_data():

        with open(settings.SITE_ROOT + "/deathstar/apps/data/initial_data.csv") as f:
            content = f.readlines()

        for line in content:
            split = line.split(';', 1)
            index = split[0]
            value = split[1]

            testObject = SensorData(stamp=index,data_line=value)
            testObject.save()

        return "Completed"

    @staticmethod
    def parse_data_string(data):
        """
        must return an array of x,y,z,type,index values
        """
        values = data.split(';')
        index = data[0]
        values = values[1:]

        result = []

        for  index, space_object in enumerate(values):
            object_data = space_object.split(',')
            object_data.append(index)
            result.append(dict(zip(['type','x','y','z','index'],object_data)))

        return result
