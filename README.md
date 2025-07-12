# Pen-To-Pi  
**Digitizing Handwritten Notes with Raspberry Pi**  

## Overview  
Pen-To-Pi is an IoT system that translates handwritten notes into digitized formats using a Raspberry Pi, camera module, and cloud-based OCR (Google Cloud Vision API). The project aims to bridge the gap between analog note-taking and digital accessibility by automating the capture, processing, and storage of handwritten content.  

## Features  
- **Automated Image Capture**: Uses a Raspberry Pi camera to photograph handwritten notes.  
- **Image Preprocessing**: Crops, rotates, and enhances images for optimal OCR accuracy.  
- **Text Recognition**: Leverages Google Cloud Vision API to extract text from images.  
- **GitHub Integration**: Stores raw images, processed images, and extracted text in a GitHub repository for easy access and searchability.  

## Setup  
1. **Hardware**:  
   - Raspberry Pi with camera module.  
   - Green masking tape (for bounding box markers).  
   - Stable desk mount for consistent image capture.  

2. **Software**:  
   - Install required Python libraries (`skimage`, `google-cloud-vision`, `PyGithub`).  
   - Set up Google Cloud Vision API credentials.  
   - Configure GitHub API access.  

3. **Run**:  
   Execute `main.py` to automate the entire pipeline (capture → process → upload).  

## Example Workflow  
1. Place handwritten notes within the green-tape bounding box.  
2. Run the script to capture and preprocess the image.  
3. The system extracts text, saves files locally, and uploads them to GitHub.  

## Results  
- Digitized notes are searchable and organized in a GitHub repository.  
- High accuracy in text recognition, even with diagrams or varied handwriting.  
- Processing time: ~15 seconds per note (cloud-dependent).  

## Repository Structure  
- `photo.py`: Captures images.  
- `scale.py`: Preprocesses and crops images.  
- `process.py`: Enhances images for OCR.  
- `words.py`: Handles text extraction via Google Cloud Vision.  
- `main.py`: Orchestrates the workflow.  
