# -- config --
TIMEOUT = 7  # seconds to wait until web service responds, 10 is AppEngine max
             # http://code.google.com/appengine/docs/python/urlfetch/fetchfunction.html
SVC = 'Python Web Site'
URL = 'http://python.org'


# -- imports --

from google.appengine.api import urlfetch


# -- the app --
print 'status of python.org services\n'

print SVC, ' - ', URL, ' - ',
try:
  result = urlfetch.fetch(URL, deadline=TIMEOUT)
except urlfetch.DeadlineExceededError:
  print 'FAIL -', 'Timeout %s exceeded' % TIMEOUT
else:
  if result.status_code == 200:
    print 'OK -', result.status_code
  else:
    print 'UNKNOWN -', result.status_code

# [ ] investigate other fetch() exceptions

