from flask import Flask
import atexit
import signal
import sys
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('flask.cfg')
from . import views, totd


def SIGTERM_handler(signum, frame):
    print('----------------got sigterm---------------')
    print('-------------exiting gracefully-----------')
    totd.save()
    sys.exit(0)

signal.signal(signal.SIGTERM, SIGTERM_handler)
totd.init()
apsched = BackgroundScheduler()
apsched.start()
apsched.add_job(totd.update, trigger='cron', hour=23, minute=28)

atexit.register(totd.save)
