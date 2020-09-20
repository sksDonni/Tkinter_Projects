from tkinter import *
from PIL import Image, ImageTk


def hiragana_method():
    hira_root = Tk()
    hira_root.title("Sensei - Hiragana")



    hira_root.mainloop()


root = Tk()
# root.minsize(800, 700)
# root.maxsize(900, 800)
root.resizable(0,0)
root.title("SENSEI")
my_title = Label(text="SENSEI", font="Helvetica 24 italic", fg="black", bg="white")
my_title.pack(fill="x")
hiragana_frame = Frame(root, borderwidth=20, padx=25, pady=30)
hiragana_frame.pack(side=LEFT, anchor=NE)

img = Image.open("images/hiragana_chi.jpg")
img = img.resize((200, 200), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)

hiragana_image_label = Label(hiragana_frame, image=img, relief=SUNKEN)
hiragana_image_label.image = img
hiragana_image_label.pack()

hiragana_button = Button(hiragana_frame, text="Practice Hiragana >>", relief=SOLID, font="Nunito 12 italic", bg="white", command=hiragana_method)
hiragana_button.pack(expand=True, fill="both")

katakana_frame = Frame(root, borderwidth=20, padx=25, pady=30)
katakana_frame.pack(side=LEFT, anchor=NE)

img = Image.open("images/katakana.png")
img = img.resize((200, 200), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)

katakana_image_label = Label(katakana_frame, image=img, relief=SUNKEN)
katakana_image_label.image = img
katakana_image_label.pack()

katakana_button = Button(katakana_frame, text="Practice Katakana >>", relief=SOLID, font="Nunito 12 italic", bg="white")
katakana_button.pack(expand=True, fill="both")

conversation_notes_frame = Frame(root, borderwidth=20, padx=25, pady=30)
conversation_notes_frame.pack(side=LEFT, anchor=NE)

img = Image.open("images/konnichiwa.jpg")
img = img.resize((200, 200), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)

conversation_image_label = Label(conversation_notes_frame, image=img, relief=SUNKEN)
conversation_image_label.image = img
conversation_image_label.pack()

conversation_button = Button(conversation_notes_frame, text="Conversation in Japanese >>", relief=SOLID, font="Nunito 12 italic", bg="white")
conversation_button.pack(expand=True, fill="both")

revision_sequence_frame = Frame(root, borderwidth=20, padx=25, pady=30)
revision_sequence_frame.pack(side=LEFT,  anchor= NE)

img = Image.open("images/revision.png")
img = img.resize((200, 200), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)

revision_sequence_label = Label(revision_sequence_frame, image=img, relief=SUNKEN)
revision_sequence_label.image = img
revision_sequence_label.pack()

revision_sequence_button = Button(revision_sequence_frame, text="Initiate revision sequence", relief=SOLID, font="Nunito 12 italic", bg="white")
revision_sequence_button.pack(expand=True, fill="both")

root.mainloop()

# grid(row=0, column=0, padx=50, pady=50)
# grid(row=0, column=1, padx=50, pady=50)