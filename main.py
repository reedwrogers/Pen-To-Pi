from github import Github
from photo import *
from scale import *
import os

# Get the image we are sending the repo
image_original = grab_photo()
image_scaled = scale(image_original)

# Replace these variables with your own information
you_know_what = 'example'
REPO_NAME = 'reedwrogers/Pen-To-Pi'

# Remove the / at the start of the file because GitHub won't take it
if image_original.startswith('/'):
    image_original = image_original[1:]
if image_scaled.startswith('/'):
    image_scaled = image_scaled[1:]

# Extract the name and extension to use
note_name_with_extension = os.path.basename(image_original)
note_name, note_ext = note_name_with_extension.rsplit('.', 1)

repo_path_original = f'Notes/{note_name}/{note_name}.{note_ext}'
repo_path_scaled = f'Notes/{note_name}/{note_name}_scaled.{note_ext}'

commit_message = f'Added original and scaled images for {note_name}.{note_ext}'

# Authenticate using an access token
g = Github(you_know_what)

# Get the repository
repo = g.get_repo(REPO_NAME)

# Read the content of the file
with open(f'/{image_original}', 'rb') as file:
    content_orig = file.read()
    
with open(f'/{image_scaled}', 'rb') as file:
    content_scaled = file.read()

# Upload the file to the repository
repo.create_file(repo_path_original, commit_message, content_orig, branch="main")
repo.create_file(repo_path_scaled, commit_message, content_scaled, branch="main")

print()
print(f"{note_name}.{note_ext} has been uploaded to {REPO_NAME} at Notes/{note_name}")