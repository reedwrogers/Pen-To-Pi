from github import Github

# Replace these variables with your own information
you_know_what = 'example'
REPO_NAME = 'reedwrogers/Pen-To-Pi'
LOCAL_FILE_PATH = '/home/reedwr/Images'
REPO_FILE_PATH = 'Notes/'  # name of resulting file
COMMIT_MESSAGE = 'Added in file'

# Authenticate using an access token
g = Github(you_know_what)

# Get the repository
repo = g.get_repo(REPO_NAME)

# Read the content of the file
with open(LOCAL_FILE_PATH, 'r') as file:
    content = file.read()

# Upload the file to the repository
repo.create_file(REPO_FILE_PATH, COMMIT_MESSAGE, content, branch="main")

print(f"{LOCAL_FILE_PATH} has been uploaded to {REPO_NAME} at {REPO_FILE_PATH}")
