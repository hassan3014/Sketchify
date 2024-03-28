import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image
import cv2
from tkinter import ttk
import os

file_path = ""
progress_var = None

def open_image():
    global file_path
    # Open a file dialog to select an image file
    file_path = filedialog.askopenfilename()

    # Load the selected image using PIL
    img = Image.open(file_path)

    # Resize the image to fit the Tkinter window
    img = img.resize((300, 300), Image.LANCZOS)

    # Create a Tkinter-compatible photo image
    photo = ImageTk.PhotoImage(img)

    # Create a label to display the image
    label.configure(image=photo)
    label.image = photo
    label.place(x=150, y=80)

    for progress in range(101):
        progress_var.set(progress)
        root.update_idletasks()

def sketchify():
    global file_path
 
    if file_path:
        # read the image
        original_image = cv2.imread(file_path)

        # confirm that image is chosen
        if original_image is None:
            print("Can not find any image. Choose appropriate file")
            return

        # Convert image to grayscale
        gray = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

        # Apply Gaussian blur to the grayscale image
        blurred = cv2.GaussianBlur(gray, (21, 21), 10)

        # Create the sketch image by blending the grayscale and blurred images
        sketch = cv2.divide(gray, blurred, scale=256.0)
#for pencil Sketch
        blur=cv2.medianBlur(gray, 5)
        invert=255-blur
        psketch = cv2.adaptiveThreshold(invert, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 2)
#for detail Sketch
        edges = cv2.Laplacian(gray, cv2.CV_8U, ksize=5)
        edges = 255 - edges
        _, dsketch = cv2.threshold(edges, 150, 255, cv2.THRESH_BINARY)
#for charcol Sketch
        filtered_image = cv2.bilateralFilter(gray, 9, 75, 75)
        chsketch = cv2.adaptiveThreshold(filtered_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 4)

        sketch_window = tk.Toplevel(root)
        sketch_window.title("Sketch Viewer")
        sketch_window.geometry("550x680")

        # Create a list to hold the image labels and save buttons
        image_labels = []

        # Display the sketch, blurred, inverted, and grayscale images
        images = [sketch,psketch,dsketch,chsketch]
        titles = ["Sketch", "Pencil Sketch", "Detail Sketch", "Charcol Sketch"]
        # Variables to keep track of row and column positions
        row_pos = 0
        col_pos = 0

        for i, (image, title) in enumerate(zip(images, titles)):
            # Resize the image to fit within the window
            resized_image = cv2.resize(image, (250, 250))

            # Convert the image to PIL format
            pil_image = Image.fromarray(resized_image)

            # Create a Tkinter-compatible photo image
            photo = ImageTk.PhotoImage(pil_image)

            # Create a label to display the image
            label = tk.Label(sketch_window, image=photo)
            label.image = photo
            label.grid(row=row_pos, column=col_pos, padx=10, pady=10)

            # Create a button to save the image
            save_button = tk.Button(sketch_window, text=f"Save {title}", command=lambda image=image, title=title: save_image(image, title))
            save_button.configure(background='#364156', foreground='white', font=('calibri', 10, 'bold'))
            save_button.grid(row=row_pos+1, column=col_pos, padx=10, pady=2)

            # Append the label and save button to the list
            image_labels.append((label, save_button))
            # Increment column position
            col_pos += 1

            # Check if column position exceeds 1, then reset to 0 and increment row position
            if col_pos > 1:
                col_pos = 0
                row_pos += 2
        if file_path:
            # Check if the captured image exists
            if os.path.exists("captured_image.jpg"):
                # Use the captured image as the input for sketching
                file_path = "captured_image.jpg"
            else:
                # The captured image doesn't exist, show an error message
                messagebox.showerror(title=None, message="No captured image found.")
                return
                  

def save_image(image, title):
    # Open a file dialog to select the save location and file name
    save_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG Image", "*.jpg"), ("PNG Image", "*.png")])

    # Check if a save location is chosen
    if save_path:
        cv2.imwrite(save_path, image)
        a = f"{title} image saved successfully at: {save_path}"
        messagebox.showinfo(title=None, message=a)

def open_camera():
    def capture_image():
        nonlocal cap

        # Read a frame from the camera
        ret, frame = cap.read()

        # Save the captured image
        file_name = "captured_image.jpg"
        cv2.imwrite(file_name, frame)

        # Release the camera and close the camera window
        cap.release()
        camera_window.destroy()

        # Display the captured image in the "Upload Image" section
        img = Image.open(file_name)
        img = img.resize((300, 300), Image.LANCZOS)
        photo = ImageTk.PhotoImage(img)
        label.configure(image=photo)
        label.image = photo
        label.place(x=150, y=80)

    # Create a camera window
    camera_window = tk.Toplevel(root)
    camera_window.title("Camera")
    camera_window.geometry("600x500")

    # Create a label to display the camera feed
    camera_label = tk.Label(camera_window)
    camera_label.pack(side='top')

    # Create a button to capture the image
    capture_button = tk.Button(camera_window, text="Capture Image", command=capture_image)
    capture_button.configure(background='#364156', foreground='white', font=('calibri', 10, 'bold'))
    capture_button.place(x=250, y=20)

    # Open the camera
    cap = cv2.VideoCapture(0)

    def update_camera():
        nonlocal cap

        # Read a frame from the camera
        ret, frame = cap.read()

        # Convert the frame to PIL format
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)

        # Resize the image to fit within the camera window
        img = img.resize((600, 500), Image.LANCZOS)

        # Create a Tkinter-compatible photo image
        photo = ImageTk.PhotoImage(img)

        # Update the camera label with the new image
        camera_label.configure(image=photo)
        camera_label.image = photo

        # Schedule the next update
        camera_window.after(10, update_camera)

    # Start updating the camera feed
    update_camera()

root = tk.Tk()
root.title("Image Viewer")
root.geometry("600x500")

# Create a label
label = tk.Label(root)
label.pack(side='top')

# Create a button to open the image
btn = tk.Button(root, text="Upload Image", command=open_image)
btn.configure(background='#364156', foreground='white', font=('calibri', 10, 'bold'))
btn.place(x=200, y=20)

# Create a button to open the camera
cam_btn = tk.Button(root, text="Open Camera", command=open_camera)
cam_btn.configure(background='#364156', foreground='white', font=('calibri', 10, 'bold'))
cam_btn.place(x=300, y=20)

progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(root, variable=progress_var, length=400)
progress_bar.place(x=100, y=450)

skbtn = tk.Button(root, text="Sketch the image", command=sketchify)
skbtn.configure(background='#364156', foreground='white', font=('calibri', 10, 'bold'))
skbtn.place(x=245, y=400)

root.mainloop()