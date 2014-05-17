#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models

class SensorData(models.Model):

    @staticmethod
    def get_latest_data():
        return [{'x':1,'y':2,'z':3}]
