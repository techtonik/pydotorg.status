'''
Probe configured web-site, store result in DB and in memcache
'''

# -- config --

TIMEOUT = 7  # seconds to wait until web service responds, 10 is AppEngine max
             # http://code.google.com/appengine/docs/python/urlfetch/fetchfunction.html
SVC = 'Python Web Site'
URL = 'http://python.org'


# -- imports ---

import logging
import time
from datetime import datetime, timedelta

from google.appengine.api import memcache
from google.appengine.api import urlfetch

import models


# -- helpers --

def check(url, timeout=TIMEOUT):
  ''' Check url status. Return triple (status, details, latency), where
      status is one of:
        OK, FAIL, WARNING, UNKNOWN
      details contain additional data and
      latency is time taken by urlfetch() call in float seconds.
  '''
  try:
    latency = time.time()
    result = urlfetch.fetch(URL, deadline=TIMEOUT)
    latency = time.time() - latency
  # [ ] investigate other fetch() exceptions
  except urlfetch.DeadlineExceededError:
    return (models.FAIL, 'Timeout exceeded (%s sec)' % TIMEOUT, float(TIMEOUT))
  else:
    status = unicode(result.status_code)
    if result.status_code == 200:
      return (models.OK, status, latency)
    else:
      return (models.UNKNOWN, status, latency)


# -- main --

def probe():
  ''' Probe site, limit attempts to one per minute, return last probe '''
  last_probe = memcache.get("last_probe")
  if last_probe == None:
    last_probe = models.Sample.all().order('-time').get()
  if (last_probe == None or
      datetime.now() - last_probe.time > timedelta(minutes=1)):
    status, details, latency = check(URL)
    last_probe = models.Sample(status=status, details=details, latency=latency)
    last_probe.put()
    if not memcache.set('last_probe', last_probe):
      logging.error('Memcache set failed for last probe.')
  return last_probe

if __name__ == '__main__':
  probe()

