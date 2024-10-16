from picamera2 import Picamera2
from datetime import datetime

# This code will need to simply save the image from the Pi when ran

def grab_photo():

    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    image_filename = f"{current_time}.jpg"

    picam2 = Picamera2()
    picam2.start_and_capture_file(image_filename)

    print(f"Image captured and saved as {image_filename}")
