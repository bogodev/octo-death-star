#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

import time


class SensorData(models.Model):

    stamp = models.PositiveIntegerField()
    data_line = models.TextField(null=True)

    @classmethod
    def get_data(cls, update, last_stamp):
        stamp = SensorData.fake_stamp();
        result, stamp = SensorData.get_data_string(stamp)
        return SensorData.parse_data_string(result), stamp

    @staticmethod
    def get_static_data():
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
    def get_data_string(index):

        try:
            dataline = SensorData.objects.get(stamp=index)
            stamp = index
        except ObjectDoesNotExist, e:
            # This is a big fat lie. the stamp changes, but the data not.
            dataline = SensorData.objects.get(stamp=1)
            stamp = index

        return dataline.data_line, stamp

    @staticmethod
    def import_test_data(version):


        if version == '1':
            path = "/deathstar/apps/data/initial_data.csv"
        elif version == '2':
            path = "/deathstar/apps/data/data_v2.csv"
        else:
            path = "/deathstar/apps/data/initial_data.csv"

        return SensorData.import_data(path)


    @staticmethod
    def import_data(path):

        SensorData.objects.all().delete()

        with open(settings.SITE_ROOT + path) as f:
            content = f.readlines()

        for line in content:
            split = line.split(';', 1)
            index = split[0]
            value = split[1].rstrip("\r\n")

            testObject = SensorData(stamp=index,data_line=value)
            testObject.save()

        return "Completed + "


    @staticmethod
    def parse_data_string(data):
        """
        must return an array of x,y,z,type,index values
        """
        values = data.split(';')
        # Remove the first position
        # values = values[1:]

        result = []

        for  index, space_object in enumerate(values):
            object_data = space_object.split(',')
            object_data.append(index)
            result.append(dict(zip(['type','x','y','z','index'],object_data)))

        return result

    @staticmethod
    def fake_stamp():
        initial_time = settings.START_TIME
        current_time = time.time()

        result = int(current_time - initial_time)
        return result


