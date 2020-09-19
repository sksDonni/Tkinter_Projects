from os import listdir
from tkinter import *
from PIL import ImageTk, Image


def get_images(path):
    global directory
    global load_images
    directory = listdir(path)
    for image in directory:
        img = Image.open(path + image)
        img = img.resize((500, 500), Image.ANTIALIAS)
        load_images.append(img)


def next_image(image_number):
    global button_forward
    global button_back
    global my_title

    print(image_number)
    my_title.grid_forget()
    img = ImageTk.PhotoImage(load_images[image_number])
    my_title = Label(image=img)
    my_title.image = img
    my_title.grid(row=0, column=0, columnspan=3)
    button_back.grid_forget()
    button_forward.grid_forget()
    if image_number >= len(load_images) - 1:
        button_forward = Button(text="Next Image", state=DISABLED)
        button_forward.grid(row=1, column=2)
        print("Disabled")
    else:
        button_forward = Button(text="Next Image", command=lambda: next_image(image_number + 1))
        button_forward.grid(row=1, column=2)

    if image_number <= 0:
        button_back = Button(text="Previous Image", state=DISABLED)
        button_back.grid(row=1, column=0)
    else:
        button_back = Button(text="Previous Image", command=lambda: prev_image(image_number - 1))
        button_back.grid(row=1, column=0)


def prev_image(image_number):

    global my_title
    global button_forward
    global button_back

    print(image_number)
    my_title.grid_forget()
    img = ImageTk.PhotoImage(load_images[image_number])
    my_title = Label(image=img)
    my_title.image = img
    my_title.grid(row=0, column=0, columnspan=3)
    button_forward.grid_forget()
    button_back.grid_forget()

    if image_number >= len(load_images) - 1:
        button_forward = Button(text="Next Image", state=DISABLED)
        button_forward.grid(row=1, column=2)
    else:
        button_forward = Button(text="Next Image", command=lambda: next_image(image_number + 1))
        button_forward.grid(row=1, column=2)

    if image_number <= 0:
        button_back = Button(text="previous image", state=DISABLED)
        button_back.grid(row=1, column=0)
    else:
        button_back = Button(text="Previous image", command=lambda: prev_image(image_number - 1))
        button_back.grid(row=1, column=0)


if __name__ == '__main__':
    # Basic initialisation

    root = Tk()

    root.title("Image Viewer")
    #root.geometry("600x600")
    path = r"C:\Users\sukrutha\Desktop\python_projects\Tkinter_Projects\imageEditor\images" + "\\"
    directory = []
    load_images = []
    my_image = Label
    get_images(path)

    button_forward = Button(text="Next Image", command=lambda: next_image(image_number + 1))
    button_forward.grid(row=1, column=2)
    button_back = Button(text="Previous Image", command=lambda: prev_image(image_number - 1))
    button_back.grid(row=1, column=0)

    img = ImageTk.PhotoImage(load_images[0])
    global my_title
    my_title = Label(image=img)
    my_title.grid(row=0, column=0, columnspan=3)
    image_number = 0

    prev_image(0)
    next_image(0)
    root.mainloop()




