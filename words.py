import os
import cv2
from google.cloud import vision

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/reed/Downloads/pen-to-pi-26fd4089263a.json"

def CloudVisionTextExtractor(handwritings):
    # Convert image from numpy to bytes for submission to Google Cloud Vision
    _, encoded_image = cv2.imencode('.jpg', handwritings)
    content = encoded_image.tobytes()
    image = vision.Image(content=content)
    
    # Feed handwriting image segment to the Google Cloud Vision API
    client = vision.ImageAnnotatorClient()
    response = client.document_text_detection(image=image)
    
    return response

def getTextAndTitleFromVisionResponse(response):
    # Extract all text and sort by top-left position for title
    texts = []
    title = ""
    top_left_word = None
    min_x = float('inf')
    min_y = float('inf')
    
    for annotation in response.text_annotations:
        text = annotation.description
        texts.append(text)
        
        # Only consider the bounding box of the first detected annotation
        if annotation == response.text_annotations[0]:
            continue

        # Bounding box coordinates
        vertices = annotation.bounding_poly.vertices
        x = vertices[0].x
        y = vertices[0].y
        
        # Check if this text is closer to the top-left
        if y < min_y or (y == min_y and x < min_x):
            min_x = x
            min_y = y
            top_left_word = text
    
    # Assign the top-left word as title
    title = top_left_word if top_left_word else ""
    return ''.join(texts), title

def get_words(path):
    # Read the image
    handwritings = cv2.imread(path)
    
    # Extract text and title
    response = CloudVisionTextExtractor(handwritings)
    text, title = getTextAndTitleFromVisionResponse(response)
    
    return text, title