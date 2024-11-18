from github import Github
from photo import *
from scale import *
from words import *
import os

# Get the image we are sending to the repo
image_original = grab_photo()
image_scaled = scale(image_original)

# Replace these variables with your own information
you_know_what = 'pwd'
REPO_NAME = 'reedwrogers/Pen-To-Pi'

# Remove the / at the start of the file because GitHub won't take it
if image_original.startswith('/'):
    image_original = image_original[1:]
if image_scaled.startswith('/'):
    image_scaled = image_scaled[1:]

words, title = get_words(f'/{image_scaled}')
print(words)
print()
print(title)

# Extract the name and extension to use
note_name_with_extension = os.path.basename(image_original)
note_name, note_ext = note_name_with_extension.rsplit('.', 1)

repo_path_original = f'Notes/{title}/{title}.{note_ext}'
repo_path_scaled = f'Notes/{title}/{title}_scaled.{note_ext}'
repo_path_text = f'Notes/{title}/{title}.txt'  # Path for the text file

commit_message = f'Added/Updated original, scaled images, and text file for {title}.{note_ext}'

# Authenticate using an access token
g = Github(you_know_what)

# Get the repository
repo = g.get_repo(REPO_NAME)

# Read the content of the image files
with open(f'/{image_original}', 'rb') as file:
    content_orig = file.read()
    
with open(f'/{image_scaled}', 'rb') as file:
    content_scaled = file.read()

# Write the contents of words to a text file
text_file_path = f'/tmp/{title}.txt'  # Temporary path for the text file
with open(text_file_path, 'w') as text_file:
    text_file.write(words)

# Read the content of the text file
with open(text_file_path, 'r') as file:
    content_text = file.read()

def upload_or_update_file(repo, path, content, message, branch="main"):
    try:
        # Check if the file already exists
        file = repo.get_contents(path, ref=branch)
        # If it exists, update it
        repo.update_file(file.path, message, content, file.sha, branch=branch)
    except Exception:
        # If it doesn't exist, create it
        repo.create_file(path, message, content, branch=branch)

# Upload or update the files
upload_or_update_file(repo, repo_path_original, content_orig, commit_message)
upload_or_update_file(repo, repo_path_scaled, content_scaled, commit_message)
upload_or_update_file(repo, repo_path_text, content_text, commit_message)

print()
print(f"{title}.{note_ext} and text file have been uploaded/updated to {REPO_NAME} at Notes/{title}")