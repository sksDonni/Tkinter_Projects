# This is the main.py file for the "SENSEI" desktop application which performs basic functions for the user to become
# a good learner of the japanese language.

# import statements - In this application we are using the Tkinter python module
from tkinter import *
from PIL import Image, ImageTk
from hiragana import HiraganaAlphabet
import io


# Methods for implementing commands from the button widgets

# the hiragana_method creates a new window to display the hiragana characters.
def hiragana_method():
    hira_root = Tk()
    hira_root.title("Sensei - Hiragana")
    filename = "arrayOfHiraganaAlphabets.txt"

    hiragana_alphabet_frame = Frame(hira_root)
    hiragana_alphabet_frame.pack(padx=50, pady=50)
    with io.open(filename, "r", encoding="utf-8") as f:
        text = f.read()
    hiragana_alphas = []
    for te in text:
        if te == "," or te == ' ':
            continue
        else:
            hiragana_alphas.append(te)

    HiraganaAlphabet(hiragana_alphabet_frame, hiragana_alphas)
    hira_root.mainloop()


# Similar to the hiragana_method, the katakana_method also creates a new window to display katakana characters

root = Tk()  # root holds the tkinter functionality
root.resizable(0, 0)  # The window is non resizeable as .... I just  wanted it this way
root.title("SENSEI")   # The title of the application

# The title label -->
my_title = Label(text="SENSEI", font="Helvetica 24 italic", fg="black", bg="white")
my_title.pack(fill="x")

# This creates the Hiragana frame which includes an image and a button to activate a new window
hiragana_frame = Frame(root, borderwidth=20, padx=25, pady=30)
hiragana_frame.pack(side=LEFT, anchor=NE)
img = Image.open("images/hiragana_chi.jpg")   # This opens the image for operations using the PIL module we imported
img = img.resize((200, 200), Image.ANTIALIAS)   # Resizes the image
img = ImageTk.PhotoImage(img)

# Hiragana label -->
hiragana_image_label = Label(hiragana_frame, image=img, relief=SUNKEN)
hiragana_image_label.image = img
hiragana_image_label.pack()

# Hiragana button -->
hiragana_button = Button(hiragana_frame, text="Practice Hiragana >>", relief=SOLID, font="Nunito 12 italic", bg="white",
                         command=hiragana_method)
hiragana_button.pack(expand=True, fill="both")


# Katakana frame, includes an image and a button to create a new window
katakana_frame = Frame(root, borderwidth=20, padx=25, pady=30)
katakana_frame.pack(side=LEFT, anchor=NE)

img = Image.open("images/katakana.png")
img = img.resize((200, 200), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)

# Katakana label -->
katakana_image_label = Label(katakana_frame, image=img, relief=SUNKEN)
katakana_image_label.image = img
katakana_image_label.pack()

# Katakana button -->
katakana_button = Button(katakana_frame, text="Practice Katakana >>", relief=SOLID, font="Nunito 12 italic", bg="white")
katakana_button.pack(expand=True, fill="both")


# Conversation frame used to display basic conversation notes.
conversation_notes_frame = Frame(root, borderwidth=20, padx=25, pady=30)
conversation_notes_frame.pack(side=LEFT, anchor=NE)

img = Image.open("images/konnichiwa.jpg")
img = img.resize((200, 200), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)

# Conversion notes label -->
conversation_image_label = Label(conversation_notes_frame, image=img, relief=SUNKEN)
conversation_image_label.image = img
conversation_image_label.pack()

# Conversion button -->
conversation_button = Button(conversation_notes_frame, text="Conversation in Japanese >>", relief=SOLID,
                             font='Nunito 12 italic', bg="white")
conversation_button.pack(expand=True, fill="both")


# Revision sequence initiation frame includes a basic revisit of concepts
revision_sequence_frame = Frame(root, borderwidth=20, padx=25, pady=30)
revision_sequence_frame.pack(side=LEFT, anchor=NE)

img = Image.open("images/revision.png")
img = img.resize((200, 200), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)

# Revision label -->
revision_sequence_label = Label(revision_sequence_frame, image=img, relief=SUNKEN)
revision_sequence_label.image = img
revision_sequence_label.pack()

# Revision button -->
revision_sequence_button = Button(revision_sequence_frame, text="Initiate revision sequence", relief=SOLID,
                                  font="Nunito 12 italic", bg="white")
revision_sequence_button.pack(expand=True, fill="both")

root.mainloop()