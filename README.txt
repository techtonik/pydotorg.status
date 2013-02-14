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
[x] limit probes to 1 request per minute
[ ] limit stored data rate to 1 record per minute
[x] store failures
[x] show last seven measurements
[ ] memcache last measurements
  [x] memcache time of the last probe
[ ] add Graphite output to index page
  [ ] show response time on Graphite graph (Y - latency, X - measurement date)
  [ ] show warnings on Graphite diagram
  [ ] show failures
[x] cron job to ping every minute
  [ ] move cron probe to a separate URL and secure access to it
    http://code.google.com/appengine/docs/python/config/cron.html
---
[ ] feature creep
  [ ] self-accessment, i.e. register warn if time between requests is more than
  [ ] port to different frameworks for comparison
  [ ] show AppEngine CPU/MEM/etc. usage on the main page
    [ ] display similar Graphite diagram when clicked
  [ ] add guard for unknown failures/exceptions
    [ ] email/xmpp unknown failures/exceptions

maintenance backlog
-------------------
[x] choose Django version explicitly to avoid complains in logs
[x] switch templates from webapp to using Django directly
[x] switch to High Replication Datastore (HRD)
[x] switch to Python 2.7
[x] switch to NDB

user story evolution
--------------------
version 1: need a service to monitor python.org site
 [x] probe that pings site every minute
 [x] web interface to see the status
version 2: optimize the code to squeeze into AppEngine quota
           (currently 1 req/minute takes 30% of CPU monthly)
 [x] avoid template rendering overhead when probing
     (CPU/sec dropped from 0.004+ to 0.003- per probe)
 (before migration to HRD and Python 2.7 cpm_usd was about 0.0055)
 (after migration to HRD cpm_usd raised to 0.012 on average)
version 3: switch to Python 2.7 and NDB


License :: Public Domain or MIT
Support :: https://groups.google.com/forum/#!forum/pydotorg
Authors ::
  anatoly techtonik <techtonik@gmail.com>


references
----------
http://code.google.com/status/appengine

http://www.pypi-mirrors.org/
https://github.com/kencochrane/pypi-mirrors
