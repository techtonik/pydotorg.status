# -- config --
TIMEOUT = 7  # seconds to wait until web service responds, 10 is AppEngine max
             # http://code.google.com/appengine/docs/python/urlfetch/fetchfunction.html
SVC = 'Python Web Site'
URL = 'http://python.org'


# -- imports --

from google.appengine.api import urlfetch
from google.appengine.ext import db
from google.appengine.ext.webapp import template

# -- helpers --
OK = 'OK'
FAIL = 'FAIL'
WARNING = 'WARNING'
UNKNOWN = 'UNKNOWN'

def check(url, timeout=TIMEOUT):
  ''' Check url status. Return pair (status, details), where
      status is one of:
        OK, FAIL, WARNING, UNKNOWN
      and details containing additional data.
  '''
  try:
    result = urlfetch.fetch(URL, deadline=TIMEOUT)
  # [ ] investigate other fetch() exceptions
  except urlfetch.DeadlineExceededError:
    return (FAIL, 'Timeout exceeded (%s sec)' % TIMEOUT)
  else:
    status = unicode(result.status_code)
    if result.status_code == 200:
      return (OK, status)
    else:
      return (UNKNOWN, status)


# -- models ---
class Sample(db.Model):
  time = db.DateTimeProperty(required=True, auto_now_add=True)
  status = db.StringProperty(required=True)
  details = db.StringProperty(required=True)


# -- the app --
title = 'status of python.org services'
status, details = check(URL)

Sample(status=status, details=details).put()

probes = Sample.all().order('-time').fetch(limit=7)

print template.render('templates/status.html',
                      dict(title=title,
                           service=SVC, url=URL, status=status, details=details,
                           probes=probes))
