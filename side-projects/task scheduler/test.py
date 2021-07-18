import schedule

def job():
    print("A simple Python Scheduler.")

schedule.every(2).seconds.do(job)

while True:
    schedule.run_pending()

