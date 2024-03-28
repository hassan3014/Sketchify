import tkinter as tk
import subprocess
from PIL import Image, ImageTk


# Create the main tkinter window
window = tk.Tk()
window.title("Sketchify")
window.geometry("600x500")

screen_width = window.winfo_screenwidth()
# print(screen_width)
screen_height = window.winfo_screenheight()
# print(screen_height)
x_pos = (screen_width // 2) - (600 // 2)  #width
y_pos = (screen_height // 2) - (500 // 2)  #height

# Set the window position to the center of the screen
window.geometry("+{}+{}".format(x_pos, y_pos))

# window.configure(bg="black")

# Set the background image
background_image = Image.open("unnamed.png")
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(window, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Add text on top of the background image
text_label = tk.Label(window, text="Sketchify", font=("Goudy Stout", 24), fg="#364156")
text_label.place(x=120, y=400)

# Create a frame to hold the buttons
frame = tk.Frame(window)
frame.pack(pady=15)

def multisketch():
    # Run the other Python file as a subprocess
    subprocess.Popen(["python", "multiplesketch.py"])

def singlesketch():
    # Run the other Python file as a subprocess
    subprocess.Popen(["python", "singlesketch.py"])


# Create the single sketch button
single_sketch_button=tk.Button(frame, text="Single Sketch", command=singlesketch, padx=10, pady=5)
single_sketch_button.configure(background='#364156', foreground='white', font=('calibri', 10, 'bold'))
single_sketch_button.pack(side=tk.LEFT, padx=0)

# Create the multiple sketch button
multiple_sketch_button = tk.Button(frame, text="Multiple Sketches", command=multisketch, padx=10, pady=5)
multiple_sketch_button.configure(background='#364156', foreground='white', font=('calibri', 10, 'bold'))
multiple_sketch_button.pack(side=tk.RIGHT, padx=1)

# Start the tkinter event loop
window.mainloop()