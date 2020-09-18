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
    print(len(load_images))


def next_image(image_number):
    global button_forward
    global my_title

    if len(load_images) >= image_number:
        my_title.pack_forget()
        img = ImageTk.PhotoImage(load_images[image_number - 1])
        my_title = Label(image=img)
        my_title.image = img
        my_title.pack()
        button_forward.pack_forget()
        button_forward = Button(text="Next Image", command=lambda: next_image(image_number + 1))
        button_forward.pack()


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

    img = ImageTk.PhotoImage(load_images[0])
    global my_title
    my_title = Label(image=img)
    my_title.pack()
    image_number = 0
    button_forward = Button(text="Next Image", command=lambda: next_image(image_number))
    button_forward.pack()

    root.mainloop()




