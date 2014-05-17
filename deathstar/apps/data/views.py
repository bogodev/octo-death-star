#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from django.http import HttpResponse
from apps.data.models import SensorData

def test_data(request):

    response_data = {}
    response_data['data'] = SensorData.get_latest_data();

    return HttpResponse(json.dumps(response_data), content_type="application/json")
