import AppCredentials #da creds
import praw # reddit API wrapper
import requests #for the URL GET requests
import os #for creating, editing and deleting files and folders
from pathlib import Path

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
            
            #convert the scrapped info to a title string, then add that string to a list of all the titles from a sub
            group = f"{SubredditGroup}"
            author = f"{submission.author}"
            title = f"{submission.title}"
            url = f"{submission.url}"
            url = url[18:]
            
            TitleVariable = url + "In r/" + group + ", u/" + author + " said: " + title + "\n"
            TitleList.append(TitleVariable)
            print(f"Title: {TitleVariable}")
            
            #add all URLs to a URL list for the memez
            print(f"Image URL: {submission.url}")
            ImageURLList.append(submission.url)

    return TitleList, ImageURLList

#given the list of image URLs of a sub, download the images
def DownloadImages(ImageURLDownloadList):
    try:
        ImageSavePath = []
        index = 0
        folder = "memez"
        Path(folder).mkdir(parents=True, exist_ok=True)
        
        for CurrentURL in ImageURLDownloadList:
            
            print(f"CurrentURL {CurrentURL}")
            ImageSavePath.append(CurrentURL[18:])
            
            ImageSavePath[index] = Path(folder) / ImageSavePath[index]
            
            # Send a GET request to the image URL
            response = requests.get(CurrentURL) #response = requests.get(ImageURLDownloadList[x])
        
            # Raise an exception if the request was not successful
            response.raise_for_status()
        
            # Write the content of the response to a file
            with open(ImageSavePath[index], 'wb') as file:
                file.write(response.content)
        
            print(f"Image successfully downloaded: {ImageSavePath[index]}")
            
            index += 1
            
    except requests.exceptions.RequestException as e:
        print(f"Failed to download the image: {e}")

def DeleteOldMemez(TitleList):
    
    ReadTitle = ""
    DeleteTitle = []
    DeleteMemeURL = ""
    
    file = open("MemeTitlez.txt", "r+", encoding="utf-8", errors="ignore")
    
    for index in file:
        ReadTitle = file.readline(index)
        CompareTitle = TitleList[index]
        
        if ReadTitle != CompareTitle:
            
            file

    
    return
    

#delete the MemeTitlez.txt file if it already exists to not have any duplicate info
def DeleteTitleFile():
    if os.path.exists("MemeTitlez.txt"):
        print("MemeTitlez.txt exists, deleting file...")
        os.remove("MemeTitlez.txt")
    else:
        print("MemeTitlez.txt does not exist")

#write the titles to the title file, so they can be used by the web front end
def WriteTitleFile(WriteTitleList):
    
    for title in WriteTitleList:
        print(f"Adding {title} to MemeTitlez.txt")
        file = open("MemeTitlez.txt", "a", encoding="utf-8", errors="ignore")
        file.write(title)
    file.close()

# call the login function
RedditCredentials = login()

#delete the MemeTitlez.txt file if it already exists to not have any duplicate info


# call each subreddit with the retrieveposts function, and store the titles 
SubredditGroup = "iiiiiiitttttttttttt"
iiiiiiittttttttttttTitleList, iiiiiiittttttttttttURLList = RetrievePosts(RedditCredentials, SubredditGroup)
if iiiiiiittttttttttttURLList:
    DownloadImages(iiiiiiittttttttttttURLList)
if iiiiiiittttttttttttTitleList:
    WriteTitleFile(iiiiiiittttttttttttTitleList)

SubredditGroup = "ProgrammerHumor"
ProgrammerHumorTitleList, ProgrammerHumorURLList = RetrievePosts(RedditCredentials, SubredditGroup)
if ProgrammerHumorURLList:
    DownloadImages(ProgrammerHumorURLList)
if ProgrammerHumorTitleList:
    WriteTitleFile(ProgrammerHumorTitleList)

SubredditGroup = "ShittySysadmin"
ShittySysadminTitleList, ShittySysadminURLList = RetrievePosts(RedditCredentials, SubredditGroup)
if ShittySysadminURLList:
    DownloadImages(ShittySysadminURLList)
if ShittySysadminURLList:
    WriteTitleFile(ShittySysadminTitleList)

SubredditGroup = "Sysadminhumor"
SysadminhumorTitleList, SysadminhumorURLList = RetrievePosts(RedditCredentials, SubredditGroup)
if SysadminhumorURLList:    
    DownloadImages(SysadminhumorURLList)
if SysadminhumorTitleList:
    WriteTitleFile(SysadminhumorTitleList)

SubredditGroup = "windowsmemes"
windowsmemesTitleList, windowsmemesURLList = RetrievePosts(RedditCredentials, SubredditGroup)
if windowsmemesURLList:
    DownloadImages(windowsmemesURLList)
if windowsmemesTitleList:
    WriteTitleFile(windowsmemesTitleList)

SubredditGroup = "cablegore"
cablegoreTitleList, cablegoreURLList = RetrievePosts(RedditCredentials, SubredditGroup)
if cablegoreURLList:
    DownloadImages(cablegoreURLList)
if cablegoreTitleList:
    WriteTitleFile(cablegoreTitleList)

SubredditGroup = "networkingmemes"
networkingmemesTitleList, networkingmemesURLList = RetrievePosts(RedditCredentials, SubredditGroup)
if networkingmemesURLList:
    DownloadImages(networkingmemesURLList)
if networkingmemesTitleList:
    WriteTitleFile(networkingmemesTitleList)

SubredditGroup = "linuxmasterrace"
linuxmasterraceTitleList, linuxmasterraceURLList = RetrievePosts(RedditCredentials, SubredditGroup)
if linuxmasterraceURLList:
    DownloadImages(linuxmasterraceURLList)
if linuxmasterraceTitleList:
    WriteTitleFile(linuxmasterraceTitleList)

SubredditGroup = "programmingmemes"
programmingmemesTitleList, programmingmemesURLList = RetrievePosts(RedditCredentials, SubredditGroup)
if programmingmemesURLList:
    DownloadImages(programmingmemesURLList)
if programmingmemesTitleList:
    WriteTitleFile(programmingmemesTitleList)