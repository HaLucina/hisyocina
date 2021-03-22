from apscheduler.schedulers.blocking import BlockingScheduler
import os
import hellow_HiSyocina
import blogTweet
import datetime

twische = BlockingScheduler()
envlist = [os.environ["CONSUMER_KEY"],
	os.environ["CONSUMER_SECRET"],
	os.environ["ACCESS_TOKEN_KEY"],
	os.environ["ACCESS_TOKEN_SECRET"]]

#twische.add_jobだと動かないのでデコードを使う
#@twische.scheduled_job('cron', hour=3, minute=5)
#def test():
#    blogTweet.upload(envlist)

# $ sleep 30 && curl https://hisyocina.herokuapp.com/ping Daily at 9:00 PM UTC
# $ curl https://hisyocina.herokuapp.com/ping Daily at 9:00 PM UTC
@twische.scheduled_job('cron', hour=6, minute=45)
def tweet_url1():
    blogTweet.upload(envlist)

# $ sleep 30 && curl https://hisyocina.herokuapp.com/ping Daily at 2:00 AM UTC
# $ curl https://hisyocina.herokuapp.com/ping Daily at 2:30 AM UT
@twische.scheduled_job('cron', hour=11, minute=45)
def tweet_url2():
    blogTweet.upload(envlist)

# $ sleep 30 && curl https://hisyocina.herokuapp.com/ping Daily at 11:00 AM UTC
# $ curl https://hisyocina.herokuapp.com/ping Daily at 11:30 AM UTC
@twische.scheduled_job('cron', hour=20, minute=45)
def tweet_url3():
    blogTweet.upload(envlist)

if __name__ == "__main__":
    timestamp = datetime.datetime.today()
    timestamp = str(timestamp.strftime("%Y/%m/%d %H:%M"))
    print('done clock.py >>> ' + timestamp)
    twische.start()
