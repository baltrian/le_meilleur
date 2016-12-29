# -*- coding: utf-8 -*-
from collections import Counter
from datetime import datetime
import json
import requests
import subprocess
import xml.etree.ElementTree

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.sites.models import Site

from djgeojson.serializers import Serializer as GeoJSONSerializer


def test(request):
	"""
	Contribute
	View to add a contribution to TrashAdvisor
	"""
	return render(request, 'consulter.html', {
	    
	})
