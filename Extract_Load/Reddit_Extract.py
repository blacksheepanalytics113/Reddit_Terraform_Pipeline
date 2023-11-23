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
       
        subreddit = reddit.subreddit("GallowBoob")
 
        # Display the name of the Subreddit
        print("Display Name:", subreddit.display_name)
        
        # Display the title of the Subreddit
        print("Title:", subreddit.title)
        
        # Display the description of the Subreddit
        # print("Description:", subreddit.description)
        df_list =[]
        subreddit = reddit.redditor("GallowBoob")
        # for post_data in subreddit.hot():
          # print(post_data)
            # Scraping the top posts of the current month
        current_month = datetime.now().month  # Get the current month
        for post in subreddit.top(time_filter="all"):
            post_month = datetime.utcfromtimestamp(post.created_utc).month
            post_month >= 1 and post_month <= current_month # Get Data Post from January Till Date
            sub_title = post.title
            sub_url = post.url
            sub_score = post.score
            sub_posts=post.id
            sub_reddit = post.subreddit
            sub_votes =post.ups
            sub_author = post.author
            sub_comments = post.num_comments
            sub_submission = post.created_utc
            print(sub_title)
            print()
            
            # Append All To Respective  Columns
            df_list.append([sub_author,sub_comments,sub_posts,sub_reddit,sub_score,sub_url,sub_votes,sub_submission,sub_title])
            
            # Create a dataframe
            reddit_df = pd.DataFrame(df_list, columns=['Author', 'Total_Comments', 'Posts', 'Reddit', 'Score','Url','Votes','Submission','Title'])
            # print(reddit_df)
        return reddit_df
    except Exception as e:
        print(e)
        sys.exit(1)
# connect_reddit()

def transform_reddit():
  reddit_transform_df = connect_reddit()
  # Transform reddit Dataframe columns 
  reddit_transform_df['Submission'] = pd.to_datetime(reddit_transform_df['Submission'])
  reddit_transform_df['Author'] = reddit_transform_df['Author'].astype(str)
  reddit_transform_df['Total_Comments'] = reddit_transform_df['Total_Comments'].astype(int)
  reddit_transform_df['Score'] = reddit_transform_df['Score'].astype(int)
  reddit_transform_df['Title'] = reddit_transform_df['Title'].astype(str)
  return reddit_transform_df
# transform_reddit()

def load_to_csv_data():
  reddit_load = transform_reddit()
  csv_path = 'C:/Users/user/Desktop/Data Engineering Projects(Personal)/AWS_Reddit_Terraform/Csv_Load/Transform_Data/reddit.csv'
  reddit_load.to_csv(csv_path, index=False)
  print(f"DataFrame successfully saved to {csv_path}")
  return reddit_load
load_to_csv_data()



    
    
    
    