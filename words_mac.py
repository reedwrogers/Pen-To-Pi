import os
import cv2
from google.cloud import vision

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/reed/Downloads/pen-to-pi-26fd4089263a.json"

def CloudVisionTextExtractor(handwritings):
    # convert image from numpy to bytes for submittion to Google Cloud Vision
    _, encoded_image = cv2.imencode('.jpg', handwritings)
    content = encoded_image.tobytes()
    image = vision.Image(content=content)
    
    # feed handwriting image segment to the Google Cloud Vision API
    client = vision.ImageAnnotatorClient()
    response = client.document_text_detection(image=image)
    
    return response

def getTextFromVisionResponse(response):
    texts = []
    for page in response.text_annotations:
        text = page.description
        texts.append(text)

    return ''.join(texts)

image_path = '/Users/reed/Desktop/Personal-Projects/Pen-To-Pi/Notes/20241114_012415/20241114_012415_scaled.jpg'
handwritings = cv2.imread(image_path)

response = CloudVisionTextExtractor(handwritings)
text = getTextFromVisionResponse(response)

print(text)