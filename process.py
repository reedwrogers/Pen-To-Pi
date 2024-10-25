from skimage import io, color, filters, exposure, img_as_ubyte
import numpy as np

def preprocess_image_for_ocr(image_path):
    # Load the image
    image = io.imread(image_path)
    
    # Convert to grayscale
    gray_image = color.rgb2gray(image)
    
    # Apply Gaussian filter to reduce noise
    blurred_image = filters.gaussian(gray_image, sigma=1.0)
    
    # Enhance contrast using adaptive histogram equalization
    enhanced_image = exposure.equalize_adapthist(blurred_image, clip_limit=0.03)
    
    # Further improve contrast by stretching the intensity values
    # Stretch the intensity values to cover the full range (0-1)
    contrast_stretched_image = exposure.rescale_intensity(enhanced_image, in_range=(0, 1), out_range=(0, 1))
    
    # Convert the image to 8-bit unsigned integer type
    contrast_stretched_image = img_as_ubyte(contrast_stretched_image)
    
    # Apply a threshold to binarize the image
    threshold = filters.threshold_otsu(contrast_stretched_image)
    binary_image = contrast_stretched_image > threshold
    
    # Invert the image so text appears white on black (if needed)
    binary_image = np.invert(binary_image)
    
    return binary_image