
from google.appengine.dist import use_library
use_library('django', '1.2')
from google.appengine.ext.webapp import template

import models
import probe

# -- the app --
title = 'status of python.org services'
last_probe = probe.probe()

# render stats for last 7 measurements
probes = models.Sample.all().order('-time').fetch(limit=7)

print template.render('templates/status.html',
                      dict(title=title,
                           service=probe.SVC, url=probe.URL,
                           status=last_probe.status, details=last_probe.details,
                           latencyms=last_probe.latency*1000,
                           probes=probes))
