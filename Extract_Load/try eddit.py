import praw
from datetime import datetime
import sys

def connect_reddit():
    print("connected to reddit!")
    try:
        reddit = praw.Reddit(client_id="Mpu0jZKmXmr8ok0Awsfqiw",
                             client_secret="ynTCE51A21217Ux9F1waBVt77T-S8w",
                             user_agent="MyAPI/0.0.1",
                             username="Ajiyee",
                             password="Olajide@1965"
                             )

        subreddit = reddit.subreddit("GallowBoob")

        # Display subreddit information
        print("Display Name:", subreddit.display_name)
        # print("Title:", subreddit.title)

        # Scraping the top posts of the current month
        current_month = datetime.now().month  # Get the current month
        for post in subreddit.top(time_filter="all"):
            post_month = datetime.utcfromtimestamp(post.created_utc).month

            if post_month >= 1 and post_month <= current_month:
                print("Title:", post.title)
                print("URL:", post.url)
                print()

    
    except Exception as e:
            print(e)
            sys.exit(1)
# Call the function
connect_reddit()
