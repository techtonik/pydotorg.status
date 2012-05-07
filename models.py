# -- models for storing data in AppEngine datastore --

from google.appengine.ext import ndb

OK = 'OK'
FAIL = 'FAIL'
WARNING = 'WARNING'
UNKNOWN = 'UNKNOWN'

class Sample(ndb.Model):
  time = ndb.DateTimeProperty(required=True, auto_now_add=True)
  # status is one of OK, FAIL, WARNING, UNKNOWN
  # [ ] try enum
  status = ndb.StringProperty(required=True)
  details = ndb.StringProperty(required=True)
  # [ ] migration for latency require=True
  latency = ndb.FloatProperty(required=False)

