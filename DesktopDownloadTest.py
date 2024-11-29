import AppCredentials
import praw
import requests

# login using reddits api keys
def login():
    print("Authenticating...")
    reddit = praw.Reddit(
        client_id = AppCredentials.client_id,
        client_secret = AppCredentials.client_secret,
        user_agent = AppCredentials.user_agent,
        redirect_uri = AppCredentials.redirect_uri
    )
    print("Authenticated as {}".format(reddit.user.me()))
    return reddit

# retrieve the top posts of the month, limited to 10, given a subreddit
def RetrievePosts(RedditCredentials, SubredditGroup):
    TitleList = []
    ImageURLList = []

    print("These posts are from " + SubredditGroup)

    for submission in RedditCredentials.subreddit(SubredditGroup).top(limit=10, time_filter="month"):
        if submission.url.endswith((".jpg", ".png")):
            print(f"Title: {submission.title}")
            TitleVariable = SubredditGroup + ": " + submission.title
            TitleList.append(TitleVariable)
            print(f"Image URL: {submission.url}")
            ImageURLList.append(submission.url)

    return TitleList, ImageURLList


# call the login function
RedditCredentials = login()

# call each subreddit with the retrieveposts function, and store the titles 
SubredditGroup = "iiiiiiitttttttttttt"
iiiiiiittttttttttttTitleList, iiiiiiittttttttttttURLList = RetrievePosts(RedditCredentials, SubredditGroup)

SubredditGroup = "ProgrammerHumor"
ProgrammerHumorTitleList, ProgrammerHumorURLList = RetrievePosts(RedditCredentials, SubredditGroup)

SubredditGroup = "ShittySysadmin"
ShittySysadminTitleList, ShittySysadminURLList = RetrievePosts(RedditCredentials, SubredditGroup)

SubredditGroup = "Sysadminhumor"
SysadminhumorTitleList, SysadminhumorURLList = RetrievePosts(RedditCredentials, SubredditGroup)

SubredditGroup = "windowsmemes"
windowsmemesTitleList, windowsmemesURLList = RetrievePosts(RedditCredentials, SubredditGroup)

SubredditGroup = "cablegore"
cablegoreTitleList, cablegoreURLList = RetrievePosts(RedditCredentials, SubredditGroup)

SubredditGroup = "networkingmemes"
networkingmemesTitleList, networkingmemesURLList = RetrievePosts(RedditCredentials, SubredditGroup)

SubredditGroup = "linuxmasterrace"
linuxmasterraceTitleList, linuxmasterraceURLList = RetrievePosts(RedditCredentials, SubredditGroup)

SubredditGroup = "programmingmemes"
programmingmemesTitleList, programmingmemesURLList = RetrievePosts(RedditCredentials, SubredditGroup)