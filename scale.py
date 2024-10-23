from photo import *
import skimage.color
import skimage.io
import numpy as np
import matplotlib.pyplot as plt

def locate_white_region(image_path):
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
            return None, None

        # Get the bounding box coordinates
        minx, maxx = int(indices_x[0]), int(indices_x[-1])
        miny, maxy = int(indices_y[0]), int(indices_y[-1])

        # Crop the original image to the detected white region
        cropped_result = image_rgb[miny:maxy, minx:maxx, :]

        # Display the results using matplotlib
        plt.figure(figsize=(10, 5))
        plt.subplot(1, 2, 1)
        plt.imshow(image_rgb)
        plt.title("Original Image")
        plt.axis('off')

        plt.subplot(1, 2, 2)
        plt.imshow(cropped_result)
        plt.title("Cropped to White Region")
        plt.axis('off')

        plt.show()

        return (minx, maxx, miny, maxy), cropped_result

    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None

# Example usage
# _,img = grab_photo()
image_path = '/home/reedwr/Pictures/Notes/20241023_051715.jpg'
bounding_box, cropped_image = locate_white_region(image_path)

if bounding_box:
    minx, maxx, miny, maxy = bounding_box
    print(f"White region bounding box: minx={minx}, maxx={maxx}, miny={miny}, maxy={maxy}")

# this needs to be fixed in a few ways:
# 1 - needs to 'return new_img_path, f'{file_name}_scaled{file_extension}', file_name' in that order
# 2- need to take away the little graphic that currently appears
# 3 - straighten the image
# 4 - allow grab_photo() to be called without error on threading
# 5 - fix up definition name and how it is called in main