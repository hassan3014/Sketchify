import cv2
import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# Function to apply Sketch effect to an image
def apply_sketch_effect(image):
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Invert the grayscale image
    inverted = cv2.bilateralFilter(gray, 9, 300, 300)

    # Apply Gaussian blur to the inverted image
    blurred = cv2.GaussianBlur(inverted, (21, 21), 10)

    # Blend the grayscale image with the blurred image using the "color dodge" blend mode
    sketch = cv2.divide(gray, blurred, scale=256.0)

    return sketch

# Function to process images in a directory
def process_images_in_directory():
   # Select the dataset directory using a file dialog
    dataset_directory = filedialog.askdirectory(title="Select Dataset Directory")

    if dataset_directory:
        # Create output directory
        output_directory = dataset_directory + "_Sketchified"
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        # Iterate over each image in the directory
        for filename in os.listdir(dataset_directory):
            if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
                # Read the image
                image_path = os.path.join(dataset_directory, filename)
                image = cv2.imread(image_path)

                # Apply Sketch effect
                Sketch_image = apply_sketch_effect(image)

                # Save the Sketchified image
                output_path = os.path.join(output_directory, filename)
                cv2.imwrite(output_path, Sketch_image)

                print(f"Processed image: {filename}")

        print("Sketch completed!")

# Create the main tkinter window
top = tk.Tk()
top.geometry('400x200')
top.title('Multiple Sketch')

screen_width = top.winfo_screenwidth()
screen_height = top.winfo_screenheight()
x_pos = (screen_width // 2)-(90 // 2)  #width
y_pos = (screen_height // 2)-(200 // 2)  #height

# Set the window position to the center of the screen
top.geometry("+{}+{}".format(x_pos, y_pos))
top.configure(background='white')

text_label = tk.Label(top, text="format ('png','jpg','jpeg')", font=("calibri", 12), fg="black",)
text_label.place(x=120, y=90)


# Function to handle the button click event
def upload_dataset():
    process_images_in_directory()

# Create the upload button
upload_button = tk.Button(top, text="Upload Folder", command=upload_dataset, padx=10, pady=5)
upload_button.configure(background='#364156', foreground='white', font=('calibri', 10, 'bold'))
upload_button.pack(pady=50)

# Start the tkinter event loop
top.mainloop()