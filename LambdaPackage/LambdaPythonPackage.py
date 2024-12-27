import boto3 # for using AWS CLI commands
import json # for formating the secrets manager credentials after they are retrieved
import praw # reddit API wrapper
import requests #for the URL GET requests
from pathlib import Path # part of the requests library

# login using reddits api keys
def login():
    print("Authenticating...")
    secret_name = "MemeDisplayinator9000RedditAPIKeys"
    secrets_client = boto3.client('secretsmanager')
    
    # Retrieve the secret value
    response = secrets_client.get_secret_value(SecretId=secret_name)
    
    # Parse the secret string (expected to be JSON)
    secret = json.loads(response['SecretString'])

    reddit = praw.Reddit(
        client_id = secret["client_id"],
        client_secret = secret["client_secret"],
        user_agent = secret["user_agent"],
        redirect_uri = secret["redirect_uri"]
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
            
            TitleVariable = url + "~/In r/" + group + ", u/" + author + " said: " + title + "\n"
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
        folder = "/tmp/memez" # tmp is the default save location for lambda
        Path(folder).mkdir(parents=True, exist_ok=True)
        
        for CurrentURL in ImageURLDownloadList:
            
            print(f"CurrentURL {CurrentURL}")
            ImageSavePath.append(CurrentURL[18:])
            
            ImageSavePath[index] = Path(folder) / ImageSavePath[index]
            
            # Send a GET request to the image URL
            response = requests.get(CurrentURL) 
        
            # Raise an exception if the request was not successful
            response.raise_for_status()
        
            # Write the content of the response to a file
            with open(ImageSavePath[index], 'wb') as file:
                file.write(response.content)
        
            print(f"Image successfully downloaded: {ImageSavePath[index]}")
            
            index += 1
            
    except requests.exceptions.RequestException as e:
        print(f"Failed to download the image: {e}")

# delete the old memes to make way for the new ones
def DeleteMemez():
    #get each item from the memez folder and store the names in the response variable
    s3_client = boto3.client('s3')
    response = s3_client.list_objects_v2(Bucket="memedisplayinator9000.com", Prefix="memez/")

    #delete each item named in the response variable
    if 'Contents' in response:
        for obj in response['Contents']:
            s3_client.delete_object(Bucket="memedisplayinator9000.com", Key=obj['Key'])
            print(f"Deleted {obj['Key']} in the memez folder")

    return {"statusCode": 200, "body": "Tasks completed successfully"}

#delete the MemeTitlez.txt file
def DeleteTitleFile():
    s3_client = boto3.client('s3')
    s3_client.delete_object(Bucket="memedisplayinator9000.com", Key="MemeTitlez.txt")
    print("Deleted MemeTitlez.txt in memedisplayinator9000.com")

#write the titles to the title file, so they can be used by the web front end
def WriteTitleFile(WriteTitleList):
    
    for title in WriteTitleList:
        print(f"Adding {title} to MemeTitlez.txt")
        file = open("/tmp/MemeTitlez.txt", "a", encoding="utf-8", errors="ignore")
        file.write(title)
    file.close()

def UploadFilesToS3():
    s3_client = boto3.client('s3')
    folder_path = "/tmp/memez" 
    folder = Path(folder_path)
    bucket_name = "memedisplayinator9000.com"
    s3_prefix = "memez"  # Optional prefix in the S3 bucket

    for file_path in folder.glob('*'): 
        s3_key = f"{s3_prefix}/{file_path.name}" if s3_prefix else file_path.name
        
        # Upload the file
        s3_client.upload_file(str(file_path), bucket_name, s3_key)
        print(f"Uploaded {file_path} to s3://{bucket_name}/{s3_key}")
    
    s3_client.upload_file("/tmp/MemeTitlez.txt", bucket_name, "MemeTitlez.txt")
    print(f"File uploaded successfully to s3://{bucket_name}/MemeTitlez.txt")
    

def LambdaHandler(event, context):
    # call the login function
    RedditCredentials = login()

    #delete the MemeTitlez.txt file if it already exists to not have any duplicate info
    DeleteTitleFile()
    DeleteMemez()

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

    UploadFilesToS3()

    return {
        "statusCode": 200,
        "body": "Lambda executed successfully!"
    }