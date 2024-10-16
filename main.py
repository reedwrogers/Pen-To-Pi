from github import Github
from photo import *

# Get the image we are sending the repo
image = grab_photo()

# Replace these variables with your own information
you_know_what = 'example'
REPO_NAME = 'reedwrogers/Pen-To-Pi'
LOCAL_FILE_PATH = f'/home/reedwr/Pictures/Notes/{image}'
REPO_FILE_PATH = f'Notes/{image}'  # name of resulting file
COMMIT_MESSAGE = 'Added in Image'



# Authenticate using an access token
g = Github(you_know_what)

# Get the repository
repo = g.get_repo(REPO_NAME)

# Read the content of the file
with open(LOCAL_FILE_PATH, 'rb') as file:
    content = file.read()

# Upload the file to the repository
repo.create_file(REPO_FILE_PATH, COMMIT_MESSAGE, content, branch="main")
print(f"{LOCAL_FILE_PATH} has been uploaded to {REPO_NAME} at {REPO_FILE_PATH}")