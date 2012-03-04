# -- config --

from probe import SVC, URL

# -- imports --

from google.appengine.dist import use_library
use_library('django', '1.2')

from google.appengine.api import memcache
from google.appengine.ext.webapp import template

from datetime import datetime, timedelta
import logging

# -- helpers --
from probe import check

# -- models ---
from models import Sample


# -- the app --
title = 'status of python.org services'


# probe site, limit attempts to one per minute
last_probe = memcache.get("last_probe")
if last_probe == None:
  last_probe = Sample.all().order('-time').get()
if (last_probe == None or
    datetime.now() - last_probe.time > timedelta(minutes=1)):
  status, details, latency = check(URL)
  last_probe = Sample(status=status, details=details, latency=latency)
  last_probe.put()
  if not memcache.set('last_probe', last_probe):
    logging.error('Memcache set failed for last probe.')

# render stats for last 7 measurements
probes = Sample.all().order('-time').fetch(limit=7)

print template.render('templates/status.html',
                      dict(title=title,
                           service=SVC, url=URL,
                           status=last_probe.status, details=last_probe.details,
                           latencyms=last_probe.latency*1000,
                           probes=probes))
