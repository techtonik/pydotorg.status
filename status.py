# -- appengine/django setup
import django.conf
import django.template.loader

if not django.conf.settings.configured:
    django.conf.settings.configure(
        TEMPLATE_DIRS=('templates',),
    )

# -- the app --
import models
import probe

title = 'status of python.org services'
last_probe = probe.probe()

# render stats for last 7 measurements
probes = models.Sample.query().order(-models.Sample.time).fetch(limit=7)

print django.template.loader.render_to_string('status.html',
                      dict(title=title,
                           service=probe.SVC, url=probe.URL,
                           status=last_probe.status, details=last_probe.details,
                           latencyms=last_probe.latency*1000,
                           probes=probes))
