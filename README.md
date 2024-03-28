## Sketchify: AI Image Sketching Project
Sketchify is a Python application built using Tkinter and OpenCV that allows users to create sketches and apply various sketch effects to images. It provides both single sketch and multiple sketch functionalities, offering an intuitive interface for digital sketching.

## Features
- **Single Sketch Mode:** Enables users to upload an image and apply various sketch effects like pencil sketch, detail sketch, and charcoal sketch.
- **Multiple Sketch Mode:** Allows users to process multiple images in a directory and apply a sketch effect to each image, saving the resulting images in a separate folder.
- **Upload Images:** Supports uploading images from both local files and live camera feed for sketching.
- **Cross-platform:** Works on Windows, macOS, and Linux platforms.

## Installation
To run Sketchify, ensure you have Python installed on your system. You can install the required dependencies using pip:
```
pip install opencv-python-headless pillow
```
Clone the repository to your local machine:
```
git clone https: //github.com/hassan3014/Sketchify.git
```
Then, you can run the main application using:
```
python main.py
```

## Usage
1. Launch the application by running `main.py`.
2. Choose between Single Sketch Mode or Multiple Sketch Mode.
   - In Single Sketch Mode, either upload an image from your local files or open the camera to capture an image. Then, click on "Sketch the image" to apply various sketch effects.
   - In Multiple Sketch Mode, upload a directory containing images (supported formats: PNG, JPEG, JPG). The application will process each image in the directory and save the Sketchified versions in a separate folder.

## Contributing
Contributions are welcome! If you have any suggestions, bug fixes, or feature requests, feel free to open an issue or submit a pull request.

## Acknowledgements
- The project uses Tkinter for the graphical user interface.
- Image processing is performed using OpenCV (Open Source Computer Vision Library).
- Image manipulation is done with Pillow, the Python Imaging Library fork.

## Contact
For any questions or inquiries, please contact [hassan.malik1574@gmail.com].

