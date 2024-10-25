import subprocess
from datetime import datetime
import os

def grab_photo():
    try:
        # Get the current time for the filename
        current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
        image_filename = f"/home/reedwr/Pictures/Notes/{current_time}.jpg"

        # Ensure the output directory exists
        os.makedirs(os.path.dirname(image_filename), exist_ok=True)

        # Capture the image using libcamera-still
        subprocess.run([
            "libcamera-still",
            "-o", image_filename,  # Output file path
            "--timeout", "2000",   # Wait for 2 seconds before capturing
            "--nopreview"          # Disable preview to avoid display issues
        ], check=True)

        print(f"Image captured and saved to {image_filename}")
        return image_filename

    except subprocess.CalledProcessError as e:
        print(f"An error occurred while capturing the image: {e}")
        return None