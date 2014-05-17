#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from django.http import HttpResponse
from apps.data.models import SensorData
from django.template import RequestContext
from django.shortcuts import render_to_response


def test_data(request):
    source = request.GET.get('source', None)

    response_data = {}

    if source == "live":
        response_data['data'] = SensorData.get_live_data()
    else:
        response_data['data'] = SensorData.get_latest_data()

    return HttpResponse(json.dumps(response_data), content_type="application/json")


def map(request):
    return render_to_response('map.html', {}, context_instance=RequestContext(request))
