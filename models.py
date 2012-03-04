# -- models for storing data in AppEngine datastore --

from google.appengine.ext import db

OK = 'OK'
FAIL = 'FAIL'
WARNING = 'WARNING'
UNKNOWN = 'UNKNOWN'

class Sample(db.Model):
  time = db.DateTimeProperty(required=True, auto_now_add=True)
  status = db.StringProperty(required=True)
  details = db.StringProperty(required=True)
  # [ ] migration for latency require=True
  latency = db.FloatProperty(required=False)

