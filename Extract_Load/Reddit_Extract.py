import sys
import requests
import numpy as np
import pandas as pd
import praw
from praw import Reddit
from datetime import datetime

def connect_reddit() -> Reddit:
    print("connected to reddit!")
    try:
        reddit = praw.Reddit(client_id= "",
                                client_secret="",
                                user_agent = "",
                                Username = "",
                                Password = ""
                                )
        subreddit = reddit.subreddit("")
 
        # Display the name of the Subreddit
        print("Display Name:", subreddit.display_name)
        
        # Display the title of the Subreddit
        print("Title:", subreddit.title)
        
        # Display the description of the Subreddit
        # print("Description:", subreddit.description)
        
        subreddit = reddit.redditor("")
        for post_data in subreddit.hot():
            print()
            # Scraping the top posts of the current month
            current_month = datetime.now().month  # Get the current month
            posts = subreddit.top(time_filter="all")
            for post in subreddit.top(time_filter="all"):
                post_month = datetime.utcfromtimestamp(post.created_utc).month

                if post_month >= 1 and post_month <= current_month:
                    # print( post.title)
                    # print(post.url)
            
            
                    posts_dictt = {"Url": [], "Post Id": [],
                      "Title": [], "Score": [],
                      "Total Comments": [], "Author": [],"Upvotes":[],
                      "Submission_Time":[],"Subreddit":[]
                      }
                    # print(posts_dictt)
            
                  # Append all data coming from post to post_dict
                    posts_dictt["Url"].append(post_data.url)
                    posts_dictt["Post Id"].append(post_data.id)
                    posts_dictt["Title"].append(post_data.title)
                    posts_dictt["Score"].append(post_data.score)
                    posts_dictt["Total Comments"].append(post_data.num_comments)
                    posts_dictt["Author"].append(post_data.author)
                    posts_dictt["Upvotes"].append(post_data.ups)
                    posts_dictt["Submission_Time"].append(post_data.created_utc)
                    posts_dictt["Subreddit"].append(post_data.subreddit)
                    # return posts_dictt
                    reddit_df = pd.DataFrame(posts_dictt)
                    # print(reddit_df)
                    return reddit_df
    except Exception as e:
        print(e)
        sys.exit(1)
# connect_reddit()

def transform_reddit():
    reddit_transform_df = connect_reddit()
    # Transform reddit Dataframe columns 
    reddit_transform_df['Submission_Time'] = pd.to_datetime(reddit_transform_df['Submission_Time'], unit='s')
    reddit_transform_df['Author'] = reddit_transform_df['Author'].astype(str)
    reddit_transform_df['Total Comments'] = reddit_transform_df['Total Comments'].astype(int)
    reddit_transform_df['Score'] = reddit_transform_df['Score'].astype(int)
    reddit_transform_df['Title'] = reddit_transform_df['Title'].astype(str)
    return reddit_transform_df
transform_reddit()
    
    
    
    