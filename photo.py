from picamera2 import Picamera2
from datetime import datetime

def grab_photo():
    try:
        current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
        image_filename = f"{current_time}.jpg"

        picam2 = Picamera2()
        # Start and capture the image
        picam2.start_and_capture_file(f'/home/reedwr/Pictures/Notes/{image_filename}')
    finally:
        # Clean up to release the camera resource
        picam2.close()
        return image_filename