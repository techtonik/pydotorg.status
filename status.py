# -- config --
TIMEOUT = 7  # seconds to wait until web service responds, 10 is AppEngine max
             # http://code.google.com/appengine/docs/python/urlfetch/fetchfunction.html
SVC = 'Python Web Site'
URL = 'http://python.org'


# -- imports --

from google.appengine.api import urlfetch


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


# -- the app --
print 'status of python.org services\n'
status, details = check(URL)
print SVC, ' - ', URL, ' - ', status, '-', details

