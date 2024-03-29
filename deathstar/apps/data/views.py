#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from django.http import HttpResponse
from apps.data.models import SensorData
from django.template import RequestContext
from django.shortcuts import render_to_response


def load_test_data(request):
    version = request.GET.get('version', '1')
    return HttpResponse(SensorData.import_test_data(version),content_type="text/plain")


def test_data(request):
    response_data = {}
    source = request.GET.get('source', None)
    # Test data
    if source == "static":
        response_data['data'] = SensorData.get_static_data();
        return HttpResponse(json.dumps(response_data), content_type="application/json")

    update = request.GET.get('update','false')
    last_stamp = request.GET.get('last_stamp',None)
    fake_data = request.GET.get('fake','false')

    if fake_data == 'true':
        fake_data = True
    else:
        fake_data = False

    if update == 'false':
        update = False

    response_data['data'], response_data['stamp'] = SensorData.get_data(update,last_stamp, fake_data)
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def map(request):
    return render_to_response('map.html', {}, context_instance=RequestContext(request))
