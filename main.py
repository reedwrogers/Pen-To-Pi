from github import Github

# Replace these variables with your own information
you_know_what = 'example'
REPO_NAME = 'https://github.com/reedwrogers/Pen-To-Pi'
FILE_PATH = 'blank.txt'
COMMIT_MESSAGE = 'Add a blank text file'

# Create a blank text file
with open(FILE_PATH, 'w') as file:
    pass

# Authenticate using an access token
g = Github(you_know_what)

# Get the repository
repo = g.get_repo(REPO_NAME)

# Read the content of the file
with open(FILE_PATH, 'r') as file:
    content = file.read()

# Upload the file to the repository
repo.create_file(FILE_PATH, COMMIT_MESSAGE, content)

print(f"{FILE_PATH} has been uploaded to {REPO_NAME}")
