from apscheduler.schedulers.blocking import BlockingScheduler
import os
import blogTweet

twische = BlockingScheduler()
envlist = [os.environ["CONSUMER_KEY"],
	os.environ["CONSUMER_SECRET"],
	os.environ["ACCESS_TOKEN_KEY"],
	os.environ["ACCESS_TOKEN_SECRET"]]

#twische.add_jobだと動かないのでデコードを使う
@twische.scheduled_job('cron', hour=7)
def tweet_url1():
    blogTweet.upload(envlist)

@twische.scheduled_job('cron', hour=12)
def tweet_url2():
    blogTweet.upload(envlist)

@twische.scheduled_job('cron', hour=20)
def tweet_url3():
    blogTweet.upload(envlist)

if __name__ == "__main__":
    print('done clock.py')
    twische.start()
