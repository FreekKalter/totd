from flask import Flask
import atexit
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('flask.cfg')
from . import views, totd

totd.init()
apsched = BackgroundScheduler()
apsched.start()
apsched.add_job(totd.update, trigger='cron', hour=23, minute=28)

atexit.register(totd.save)
