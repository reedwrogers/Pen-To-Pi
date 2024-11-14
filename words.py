from PIL import Image
import pytesseract
import numpy as np

# THIS MODEL DOESN'T WORK!

def get_words(image_path):
    try:
        image_path = f'/{image_path}'
        # Open the image using Pillow
        img = Image.open(image_path)
        
        # Rotate the image 90 degrees to the left
        rotated_img = img.rotate(90, expand=True)  # `expand=True` ensures the entire rotated image is included
        
        # Perform OCR using Tesseract on the rotated image
        text = pytesseract.image_to_string(rotated_img)
        
        # Split the extracted text into words
        words = text.split()
        
        # Optionally, strip any leading/trailing punctuation from each word
        words = [word.strip('.,!?"\'') for word in words]
        
        return words
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return []  # Return empty list on failure