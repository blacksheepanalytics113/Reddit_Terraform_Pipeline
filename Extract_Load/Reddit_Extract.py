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
                                user_agent = "MyAPI/0.0.1",
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
        
        subreddit = reddit.redditor("GallowBoob")
        # for post_data in subreddit.hot():
          # print(post_data)
            # Scraping the top posts of the current month
        current_month = datetime.now().month  # Get the current month
        for post in subreddit.top(time_filter="all"):
            post_month = datetime.utcfromtimestamp(post.created_utc).month
            post_month >= 1 and post_month <= current_month # Get Data Post from January Till Date
            # print(post.title)
            print()
          
            # print(post.url)
            posts_dictt = {"Url": [], "Post Id": [],
              "Title": [], "Score": [],
              "Total Comments": [], "Author": [],"Upvotes":[],
              "Submission_Time":[],"Subreddit":[]
              }
                
            
                  # Append all data coming from post to post_dict
            posts_dictt["Url"].append(post.url)
            posts_dictt["Post Id"].append(post.id)
            posts_dictt["Title"].append(post.title)
            posts_dictt["Score"].append(post.score)
            posts_dictt["Total Comments"].append(post.num_comments)
            posts_dictt["Author"].append(post.author)
            posts_dictt["Upvotes"].append(post.ups) 
            posts_dictt["Submission_Time"].append(post.created_utc)
            posts_dictt["Subreddit"].append(post.subreddit)
            
            # print(posts_dictt)
            
            # Initialize an empty DataFrame
            final_df = pd.DataFrame()

            # Convert each JSON into a DataFrame and append it to the final DataFrame
            temp_df = pd.json_normalize(posts_dictt)
            print(temp_df)
           

            # final_df = final_df.a(temp_df, ignore_index=True)
            # print(final_df)

           
            csv_path = 'C:/Users/user/Desktop/Data Engineering Projects(Personal)/AWS_Reddit_Terraform/Csv_Load/Raw_Data/reddit.csv'
            temp_df.to_csv(csv_path, index=True)
            print(f"DataFrame successfully saved to {csv_path}")
                    
   
                    # return reddit_df
    except Exception as e:
        print(e)
        sys.exit(1)
connect_reddit()

def transform_reddit():
  reddit_transform_df = connect_reddit()
  # print(reddit_df)
  # Transform reddit Dataframe columns 
  reddit_transform_df['Submission_Time'] = pd.to_datetime(reddit_transform_df['Submission_Time'])
  reddit_transform_df['Author'] = reddit_transform_df['Author'].astype(str)
  reddit_transform_df['Total Comments'] = reddit_transform_df['Total Comments'].astype(int)
  reddit_transform_df['Score'] = reddit_transform_df['Score'].astype(int)
  reddit_transform_df['Title'] = reddit_transform_df['Title'].astype(str)
  # return reddit_transform_df
  return reddit_transform_df
transform_reddit()

def load_to_csv_data():
  reddit_load = transform_reddit()
  csv_path = 'C:/Users/user/Desktop/Data Engineering Projects(Personal)/AWS_Reddit_Terraform/Csv_Load/reddit.csv'
  reddit_load.to_csv(csv_path, index=False)
  print(f"DataFrame successfully saved to {csv_path}")
  return reddit_load
load_to_csv_data()



    
    
    
    