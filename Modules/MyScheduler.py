from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
import requests
import os
def sensor():
    url=os.environ.get("ALIVE",None)
    r = requests.get(url)
    print(r.text)  

def MyScheduler():
    sched = BackgroundScheduler(daemon=True)
    interval = IntervalTrigger(
        minutes = 1,
        start_date='2019-4-24 08:00:00',
        end_date='2099-4-24 08:00:00',
        timezone='Asia/Shanghai')
    sched.add_job(sensor,trigger=interval)
    sched.start()
    return ''