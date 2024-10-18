import cv2
import os
import numpy as np

#-----------
# Maybe a better way to do this would be to use an item detection model that can detect a piece of paper.. or a whiteboard.. 
# ----------

# Capture image and convert to grayscale
def scale(img_path):

    file_name, file_extension = os.path.splitext(img_path)
    
    image = cv2.imread(f'/home/reedwr/Pictures/Notes/{img_path}')

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply edge detection
    edges = cv2.Canny(gray, 50, 150)

    # Find contours to get the largest rectangle
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Iterate over the detected contours to find one that is approximately rectangular and large enough to be the notebook
    page_contour = None
    for contour in contours:
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        if len(approx) == 4:  # Rectangle has 4 sides
            page_contour = approx
            break

    # If a rectangle contour is found, apply a perspective transformation to warp the image so that the page appears flat and scaled to a consistent size
    if page_contour is not None:
        pts = page_contour.reshape(4, 2)
        # Reorder points for perspective transform
        rect = cv2.boundingRect(pts)
        dst_pts = np.array([[0, 0], [rect[2], 0], [rect[2], rect[3]], [0, rect[3]]], dtype="float32")
        M = cv2.getPerspectiveTransform(pts.astype("float32"), dst_pts)
        warped = cv2.warpPerspective(image, M, (rect[2], rect[3]))

    # Ensure the transformed image is always resized to a standard resolution
    standard_size = (800, 600)  # Choose your preferred dimensions
    resized = cv2.resize(warped, standard_size)

    new_img_path = f"/home/reedwr/Pictures/Notes/{file_name}_scaled{file_extension}"

    cv2.imwrite(new_img_path, resized)
    
    new_img_path = f"home/reedwr/Pictures/Notes/{file_name}_scaled{file_extension}"

    return new_img_path, f'{file_name}_scaled{file_extension}', file_name