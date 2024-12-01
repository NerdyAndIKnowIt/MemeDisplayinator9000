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
            
            group = f"{SubredditGroup}"
            author = f"{submission.author}"
            title = f"{submission.title}"
            
            TitleVariable = "In r/" + group + ", u/" + author + " said: " + title
            TitleList.append(TitleVariable)
            print(f"Title: {TitleVariable}")
            
            print(f"Image URL: {submission.url}")
            ImageURLList.append(submission.url)

    return TitleList, ImageURLList

#given the list of image URLs of a sub, download the images
def DownloadImages(ImageURLDownloadList):
    try:
        
        ImageSavePath = []
        x = 0
        
        for x in ImageURLDownloadList:
            
            CurrentURL = ImageURLDownloadList[x]
            
            ImageSavePath[x] = CurrentURL[18:]
            
            # Send a GET request to the image URL
            response = requests.get(ImageURLDownloadList[x])
        
            # Raise an exception if the request was not successful
            response.raise_for_status()
        
            # Write the content of the response to a file
            with open(ImageSavePath[x], 'wb') as file:
                file.write(response.content)
        
            print(f"Image successfully downloaded: {ImageSavePath[x]}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download the image: {e}")


# call the login function
RedditCredentials = login()

# call each subreddit with the retrieveposts function, and store the titles 
SubredditGroup = "iiiiiiitttttttttttt"
iiiiiiittttttttttttTitleList, iiiiiiittttttttttttURLList = RetrievePosts(RedditCredentials, SubredditGroup)
if iiiiiiittttttttttttURLList:
    DownloadImages(iiiiiiittttttttttttURLList)

SubredditGroup = "ProgrammerHumor"
ProgrammerHumorTitleList, ProgrammerHumorURLList = RetrievePosts(RedditCredentials, SubredditGroup)
if ProgrammerHumorURLList:
    DownloadImages(ProgrammerHumorURLList)

SubredditGroup = "ShittySysadmin"
ShittySysadminTitleList, ShittySysadminURLList = RetrievePosts(RedditCredentials, SubredditGroup)
if ShittySysadminURLList:
    DownloadImages(ShittySysadminURLList)

SubredditGroup = "Sysadminhumor"
SysadminhumorTitleList, SysadminhumorURLList = RetrievePosts(RedditCredentials, SubredditGroup)
if SysadminhumorURLList:    
    DownloadImages(SysadminhumorURLList)

SubredditGroup = "windowsmemes"
windowsmemesTitleList, windowsmemesURLList = RetrievePosts(RedditCredentials, SubredditGroup)
if windowsmemesURLList:
    DownloadImages(windowsmemesURLList)

SubredditGroup = "cablegore"
cablegoreTitleList, cablegoreURLList = RetrievePosts(RedditCredentials, SubredditGroup)
if cablegoreURLList:
    DownloadImages(cablegoreURLList)

SubredditGroup = "networkingmemes"
networkingmemesTitleList, networkingmemesURLList = RetrievePosts(RedditCredentials, SubredditGroup)
if networkingmemesURLList:
    DownloadImages(networkingmemesURLList)

SubredditGroup = "linuxmasterrace"
linuxmasterraceTitleList, linuxmasterraceURLList = RetrievePosts(RedditCredentials, SubredditGroup)
if linuxmasterraceURLList:
    DownloadImages(linuxmasterraceURLList)

SubredditGroup = "programmingmemes"
programmingmemesTitleList, programmingmemesURLList = RetrievePosts(RedditCredentials, SubredditGroup)
if programmingmemesURLList:
    DownloadImages(programmingmemesURLList)