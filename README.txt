
monitor status of python.org services


design and task backlog
-----------------------
[x] use AppEngine (no hosting, easy to setup and upload, high availability)
[ ] create page that downloads www.python.org and prints response time
  [ ] use URL Fetch API http://code.google.com/appengine/docs/python/urlfetch/
  [ ] process exceptions (needs two levels - warning and fails)
    [ ] download size exceeded sane amount (hardcoded 200k)
    [ ] timeout fail
    [ ] warning if response is too slow (hardcoded 5 seconds)
[ ] store response time in DB
[ ] store failures 
[ ] show last seven measurements
[ ] memcache last measurements
[ ] add Graphite output to index page
  [ ] show response time on Graphite graph (Y - latency, X - measurement date)
  [ ] show warnings on Graphite diagram
  [ ] show failures
[ ] cron job to ping every minute


License :: Public Domain or MIT
Support :: https://groups.google.com/forum/#!forum/pydotorg
Authors ::
  anatoly techtonik <techtonik@gmail.com>


references
----------
http://code.google.com/status/appengine
