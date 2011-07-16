# -- config --
TIMEOUT = 7  # seconds to wait until web service responds, 10 is AppEngine max
             # http://code.google.com/appengine/docs/python/urlfetch/fetchfunction.html
SVC = 'Python Web Site'
URL = 'http://python.org'


# -- imports --

from google.appengine.api import urlfetch
from google.appengine.ext import db

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
    if result.status_code == 200:
      return (OK, result.status_code)
    else:
      return (UNKNOWN, result.status_code)


# -- models ---
class Sample(db.Model):
  time = db.DateTimeProperty(required=True, auto_now_add=True)
  status = db.StringProperty(required=True)
  details = db.StringProperty(required=True)


# -- the app --
print 'status of python.org services\n'
status, details = check(URL)
print SVC, ' - ', URL, ' - ', status, '-', details

Sample(status=status, details=details).put()

print 'last 7 probes: ',
print [x.status for x in Sample.all().order('-time').fetch(limit=7)]
