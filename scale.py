import skimage.color
import skimage.io
import numpy as np
import cv2
from photo import *
import os

def scale(image_path):
    try:        
        # Read the image
        image_rgb = skimage.io.imread(image_path)

        # Convert the image to HSV color space
        image_hsv = skimage.color.rgb2hsv(image_rgb)

        # Threshold based on the V (brightness) channel
        white_threshold = 0.85
        white_mask = image_hsv[:, :, 2] > white_threshold

        # Find the bounding box of the white region
        mask_x = white_mask.max(axis=0)
        mask_y = white_mask.max(axis=1)
        indices_x = mask_x.nonzero()[0]
        indices_y = mask_y.nonzero()[0]

        # If no white region is found, return an error
        if indices_x.size == 0 or indices_y.size == 0:
            print("No white region detected in the image.")
            return None, None, None

        # Get the bounding box coordinates
        minx, maxx = int(indices_x[0]), int(indices_x[-1])
        miny, maxy = int(indices_y[0]), int(indices_y[-1])

        # Crop the original image to the detected white region
        cropped_result = image_rgb[miny:maxy, minx:maxx, :]
        
        # Save the processed image
        scaled_file_name_with_extension = os.path.basename(image_path)
        scaled_file_name, scaled_file_extension = scaled_file_name_with_extension.rsplit('.', 1)        
        scaled_output_path = f"/home/reedwr/Pictures/Notes/{scaled_file_name}_scaled.{scaled_file_extension}"
        skimage.io.imsave(scaled_output_path, cropped_result)
        
        return scaled_output_path

    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None, None