
monitor status of python.org services


design and task backlog
-----------------------
[x] use AppEngine (no hosting, easy to setup and upload, high availability)
[ ] create page that downloads www.python.org and prints response time
  [x] use URL Fetch API http://code.google.com/appengine/docs/python/urlfetch/
  [ ] process exceptions (needs two levels - warning and fails)
    [ ] download size exceeded sane amount (hardcoded 200k)
    [x] timeout fail
    [ ] warning if response is too slow (hardcoded 5 seconds)
[x] store response time in DB
[ ] limit stored data rate to 1 record per minute
[x] store failures
[x] show last seven measurements
[ ] memcache last measurements
[ ] add Graphite output to index page
  [ ] show response time on Graphite graph (Y - latency, X - measurement date)
  [ ] show warnings on Graphite diagram
  [ ] show failures
[ ] cron job to ping every minute
    http://code.google.com/appengine/docs/python/config/cron.html
---
[ ] feature creep
  [ ] self-accessment, i.e. register warn if time between requests is more than
  [ ] port to different frameworks for comparison
  [ ] show AppEngine CPU/MEM/etc. usage on the main page
    [ ] display similar Graphite diagram when clicked
  [ ] add guard for unknown failures/exceptions
    [ ] email/xmpp unknown failures/exceptions



License :: Public Domain or MIT
Support :: https://groups.google.com/forum/#!forum/pydotorg
Authors ::
  anatoly techtonik <techtonik@gmail.com>


references
----------
http://code.google.com/status/appengine
