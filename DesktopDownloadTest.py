import credentials
import praw


def login():
     LoginCredentials = praw.Reddit(
        #username = credentials.username,
        #password = credentials.password,
        client_id = credentials.client_id,
        client_secret = credentials.client_secret,
        user_agent = credentials.user_agent)
     return LoginCredentials

def RetrievePosts(RedditCredentials, SubredditGroup):
    for submission in RedditCredentials.subreddit(SubredditGroup).top(limit=10):
        print(f"test")
        if submission.url.endswith((".jpg", ".png")):
            print(f"test")
            print(f"Title: {submission.title}")
            print(f"Image URL: {submission.url}")

RedditCredentials = login()

print(RedditCredentials.user.me())

#SubredditGroup = "iiiiiiitttttttttttt"
#RetrievePosts(RedditCredentials, SubredditGroup)

#SubredditGroup = "ProgrammerHumor"
#RetrievePosts(RedditCredentials, SubredditGroup)
#subreddit = reddit.subreddit("ProgrammerHumor")

