# This is the main.py file for the "SENSEI" desktop application which performs basic functions for the user to become
# a good learner of the japanese language.

# import statements - In this application we are using the Tkinter python module
from tkinter import *
from PIL import Image, ImageTk
from hiragana import PrintAlphabet


# Methods for implementing commands from the button widgets

# the alphabet_method creates a new window to display the hiragana characters.
def alphabet_method():
    alphabet_root = Tk()
    alphabet_root.title("Sensei - Hiragana and katakana")
    alphabet_root.resizable(0, 0)
    P = PrintAlphabet(alphabet_root)
    filename1 = "arrayOfHiraganaAlphabets.txt"
    filename2 = "arrayOfKatakanaAlphabets.txt"
    button_frame_for_alphabets = Frame(alphabet_root)
    hiragana_frame = Frame(alphabet_root)
    katakana_frame = Frame(alphabet_root)
    button_frame_for_alphabets.grid(row=0, column=0)

    for frame in (hiragana_frame, katakana_frame):
        frame.grid(row=1, column=0)

    show_hiragana_button = Button(button_frame_for_alphabets, text="hiragana", command=lambda: P.show_alphabet(alphabet_root, hiragana_frame, filename1), font="Helvetica 20 italic")
    show_hiragana_button.pack(side=LEFT, padx=20, fill="x")
    show_katakana_button = Button(button_frame_for_alphabets, text="katakana", command=lambda:  P.show_alphabet(alphabet_root, katakana_frame, filename2), font="Helvetica 20 italic")
    show_katakana_button.pack(side=LEFT, padx=20, fill="x")
    alphabet_root.mainloop()


# Similar to the alphabet_method, the katakana_method also creates a new window to display katakana characters

root = Tk()  # root holds the tkinter functionality
root.resizable(0, 0)  # The window is non resizeable as .... I just  wanted it this way
root.title("SENSEI")  # The title of the application

# The title label -->
my_title = Label(text="SENSEI", font="Helvetica 24 italic", fg="black", bg="white")
my_title.pack(fill="x")

# This creates the Hiragana frame which includes an image and a button to activate a new window
alphabet_frame = Frame(root, borderwidth=20, padx=25, pady=30)
alphabet_frame.pack(side=LEFT, anchor=NE)
img = Image.open("images/hiragana_chi.jpg")  # This opens the image for operations using the PIL module we imported
img = img.resize((200, 200), Image.ANTIALIAS)  # Resizes the image
img = ImageTk.PhotoImage(img)

# Hiragana label -->
alphabet_image_label = Label(alphabet_frame, image=img, relief=SUNKEN)
alphabet_image_label.image = img
alphabet_image_label.pack()

# Hiragana button -->
alphabet_button = Button(alphabet_frame, text="Practice Hiragana and Katakana", relief=SOLID, font="Nunito 12 italic",
                         bg="white", command=alphabet_method)
alphabet_button.pack(expand=True, fill="both")

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
