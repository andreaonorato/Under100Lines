from io import BytesIO
from tkinter import *
from tkinter import messagebox
from captcha.image import ImageCaptcha
from random import randint

# Initialize ImageCaptcha with custom fonts
image = ImageCaptcha(fonts=['fonts/ChelseaMarketsr.ttf', 'fonts/DejaVuSanssr.ttf'])

# Generate a random 6-digit number for the captcha
captcha_value = str(randint(100000, 999999))

# Generate the captcha image data and save it to a file
data = image.generate(captcha_value)
assert isinstance(data, BytesIO)
image.write(captcha_value, 'out.png')

def verify():
    """Verify the entered captcha value."""
    global captcha_value
    entered_value = t1.get("0.0", END).strip()  # Get the entered value
    if entered_value == captcha_value:
        messagebox.showinfo("Success", "Verified")
    else:
        messagebox.showinfo("Alert", "Not Verified")
        refresh()

def refresh():
    """Generate a new captcha and update the displayed image."""
    global captcha_value
    captcha_value = str(randint(100000, 999999))  # Generate new captcha value
    data = image.generate(captcha_value)  # Generate new captcha image data
    assert isinstance(data, BytesIO)
    image.write(captcha_value, 'out.png')  # Save new captcha image
    photo = PhotoImage(file="out.png")  # Load the new captcha image
    l1.config(image=photo)  # Update the label with the new image
    l1.image = photo  # Keep a reference to avoid garbage collection

# Create the main Tkinter window
root = Tk()

# Load the initial captcha image
photo = PhotoImage(file="out.png")

# Create GUI elements
l1 = Label(root, image=photo, height=100, width=200)
t1 = Text(root, height=5, width=50)
b1 = Button(root, text="Submit", command=verify)
b2 = Button(root, text="Refresh", command=refresh)

# Pack GUI elements
l1.pack()
t1.pack()
b1.pack()
b2.pack()

# Start the Tkinter event loop
root.mainloop()
