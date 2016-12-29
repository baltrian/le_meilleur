# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from collections import defaultdict, Counter

from django.db import models
from django.db.models import Count
from django.contrib.gis.db import models as gis_models
from django.utils.text import slugify


