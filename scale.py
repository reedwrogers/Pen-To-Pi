import skimage.color
import skimage.io
import numpy as np
import os
from skimage import draw
from process import preprocess_image_for_ocr
from PIL import Image  

def scale(image_path):
    try:        
        # Read the image
        image_rgb = skimage.io.imread(image_path)

        # Convert the image to HSV color space
        image_hsv = skimage.color.rgb2hsv(image_rgb)

        # Define the green color range (tune if necessary)
        lower_green = np.array([0.25, 0.3, 0.3])  # Adjust hue, saturation, and value
        upper_green = np.array([0.45, 1.0, 1.0])

        # Create a mask for the green color
        green_mask = (image_hsv[:, :, 0] >= lower_green[0]) & (image_hsv[:, :, 0] <= upper_green[0]) & \
                     (image_hsv[:, :, 1] >= lower_green[1]) & (image_hsv[:, :, 1] <= upper_green[1]) & \
                     (image_hsv[:, :, 2] >= lower_green[2]) & (image_hsv[:, :, 2] <= upper_green[2])

        # Find the bounding box of the green region
        mask_x = green_mask.max(axis=0)
        mask_y = green_mask.max(axis=1)
        indices_x = mask_x.nonzero()[0]
        indices_y = mask_y.nonzero()[0]

        # If no green region is found, return an error
        if indices_x.size == 0 or indices_y.size == 0:
            print("No green region detected in the image.")
            return None

        # Get the bounding box coordinates
        minx, maxx = int(indices_x[0]), int(indices_x[-1])
        miny, maxy = int(indices_y[0]), int(indices_y[-1])

        # Crop the original image to the detected green region
        cropped_result = image_rgb[miny:maxy, minx:maxx, :]
        
        # Save the cropped image for verification
        scaled_file_name_with_extension = os.path.basename(image_path)
        scaled_file_name, scaled_file_extension = scaled_file_name_with_extension.rsplit('.', 1)
        scaled_output_path = f"/home/reedwr/Pictures/Notes/{scaled_file_name}_scaled.{scaled_file_extension}"
        skimage.io.imsave(scaled_output_path, cropped_result)
        skimage.io.imsave(f"/home/reedwr/Pictures/Notes/{scaled_file_name}_scaled_before_proc.{scaled_file_extension}", cropped_result)

        # Preprocess the image for OCR
        processed_image = preprocess_image_for_ocr(scaled_output_path)

        # Rotate the image 90 degrees
        rotated_image = np.rot90(processed_image, -1)  # 1 is clockwise, -1 is counter-clockwise
        
        # Save the rotated image
        rotated_output_path = f"/home/reedwr/Pictures/Notes/{scaled_file_name}_scaled_rotated.{scaled_file_extension}"
        skimage.io.imsave(rotated_output_path, rotated_image)
        
        return rotated_output_path

    except Exception as e:
        print(f"An error occurred: {e}")
        return None