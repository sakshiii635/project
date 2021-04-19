from apscheduler.schedulers.blocking import BlockingScheduler
from MajorProject import maintask
def some_job():
    print("Job Started")
    maintask()

scheduler = BlockingScheduler()
scheduler.add_job(some_job, 'interval', seconds=20)
scheduler.start()