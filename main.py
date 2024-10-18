from github import Github
from photo import *
from scale import *

# Get the image we are sending the repo
image_original = grab_photo()
image_scaled = scale(image_original)

# Replace these variables with your own information
you_know_what = 'example'
REPO_NAME = 'reedwrogers/Pen-To-Pi'
LOCAL_FILE_PATH, NOTE_NAME_EXT, NOTE_NAME = image_scaled
REPO_FILE_PATH = f'Notes/{NOTE_NAME}/{NOTE_NAME_EXT}'  # name of resulting file
COMMIT_MESSAGE = 'Added in Image'

# Authenticate using an access token
g = Github(you_know_what)

# Get the repository
repo = g.get_repo(REPO_NAME)

# Read the content of the file
with open(f'/{LOCAL_FILE_PATH}', 'rb') as file:
    content = file.read()

# Upload the file to the repository
repo.create_file(REPO_FILE_PATH, COMMIT_MESSAGE, content, branch="main")
print(f"{NOTE_NAME_EXT} has been uploaded to {REPO_NAME} at {REPO_FILE_PATH}")