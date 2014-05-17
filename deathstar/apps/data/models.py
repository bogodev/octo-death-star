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

    @staticmethod
    def get_live_data():
        return SensorData.parse_data_string(SensorData.get_data_string(1))

    @staticmethod
    def get_data_string(index):
        return "1;O,5135,5042,5000;M,10000,10000,10000"

    @staticmethod
    def parse_data_string(data):
        """
        must return an array of x,y,z,type,index values
        """
        values = data.split(';')
        index = data[0]
        values = values[1:]

        result = []

        for space_object in values:
            object_data = space_object.split(',')
            result.append(dict(zip(['type','x','y','z'],object_data)))

        return result
