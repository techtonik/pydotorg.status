# -- config --
TIMEOUT = 7  # seconds to wait until web service responds, 10 is AppEngine max
             # http://code.google.com/appengine/docs/python/urlfetch/fetchfunction.html
SVC = 'Python Web Site'
URL = 'http://python.org'

# -- imports ---

from google.appengine.api import urlfetch

from models import OK, FAIL, WARNING, UNKNOWN

# -- helpers --

def check(url, timeout=TIMEOUT):
  ''' Check url status. Return triple (status, details, latency), where
      status is one of:
        OK, FAIL, WARNING, UNKNOWN
      details contain additional data and
      latency is time taken by urlfetch() call in float seconds.
  '''
  import time
  try:
    latency = time.time()
    result = urlfetch.fetch(URL, deadline=TIMEOUT)
    latency = time.time() - latency
  # [ ] investigate other fetch() exceptions
  except urlfetch.DeadlineExceededError:
    return (FAIL, 'Timeout exceeded (%s sec)' % TIMEOUT, float(TIMEOUT))
  else:
    status = unicode(result.status_code)
    if result.status_code == 200:
      return (OK, status, latency)
    else:
      return (UNKNOWN, status, latency)

# -- main --


