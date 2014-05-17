#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from django.http import HttpResponse
from apps.data.models import SensorData


def load_test_data(request):

    return HttpResponse(SensorData.import_test_data(),content_type="text/plain")


def test_data(request):
    response_data = {}

    source = request.GET.get('source',None)
    # Test data
    if source == "static":
        response_data['data'] = SensorData.get_static_data();
        return HttpResponse(json.dumps(response_data), content_type="application/json")

    update = request.GET.get('update','false')
    last_stamp = request.GET.get('last_stamp',None)

    if update == 'false':
        update = False

    response_data['data'], response_data['stamp'] = SensorData.get_data(update,last_stamp)

    return HttpResponse(json.dumps(response_data), content_type="application/json")
