# -- config --

from probe import SVC, URL

# -- imports --

from google.appengine.dist import use_library
use_library('django', '1.2')

from google.appengine.ext.webapp import template

# -- helpers --
import probe

# -- models ---
from models import Sample


# -- the app --
title = 'status of python.org services'
last_probe = probe.probe()

# render stats for last 7 measurements
probes = Sample.all().order('-time').fetch(limit=7)

print template.render('templates/status.html',
                      dict(title=title,
                           service=SVC, url=URL,
                           status=last_probe.status, details=last_probe.details,
                           latencyms=last_probe.latency*1000,
                           probes=probes))
