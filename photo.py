from picamera2 import Picamera2
from datetime import datetime

# This code will save the image from the Pi when run

def grab_photo():
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    image_filename = f"{current_time}.jpg"

    picam2 = Picamera2()
    picam2.start_and_capture_file(f'/home/reedwr/Pictures/Notes/{image_filename}')

    return image_filename

# Call the function to capture the photo
grab_photo()

