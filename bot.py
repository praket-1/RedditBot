import praw
import random
import time

reddit = praw.Reddit(  #R should be in capital.
    client_id='lRm-D_ewb-dcPiPxeHrLwg',
    client_secret='3mzpdLxffARjez0MumLhIGgXE99FMg',
    user_agent='Bot Testing by /u/MalencholicBot',
    username='MalencholicBot',
    password='AVm>UKE5~sX2R#9')

subreddit = reddit.subreddit("copypasta")

quotes = [
          ]


for submission in subreddit.hot(limit = 10):
    print('..........')
    print(submission.title)

    for comment in submission.comments:
        if hasattr(comment,"body"):
            comment_lower = comment.body.lower()
            if " sad " in comment_lower:
                print("---------------")
                print(comment.body)

                random_index = random.randint(0,len(quotes) - 1)

                comment.reply(quotes[random_index])
                time.sleep(30)