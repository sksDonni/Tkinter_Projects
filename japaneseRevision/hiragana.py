from tkinter import *
from PIL import Image, ImageTk

class HiraganaAlphabet:

    def __init__(self, root, text):
        self.root = root
        self.text = text
        i = 0
        k = 0
        global j
        j = 0

        for j in range(0, len(text)):
            if text[j].encode("utf-8") == "が".encode("utf-8"):
                for i in range(0, 10):
                    dash = Label(root, text="||")
                    dash.grid(row=i, column=5)

                temp = j
                w = 2
                k = 6
                for j in range(temp, len(text)):
                    if j % 5 == 0:
                        w += 1
                        k = 6
                    label = Label(root, text=text[j], font="Helvetica 24 bold")
                    label.grid(row=w, column=k, padx=10, pady=10)
                    k += 1
                break

            if j % 5 == 0 and j != 0:
                i += 1
                k = 0
            label = Label(root, text=text[j], font="Helvetica 24 bold")
            label.grid(row=i, column=k, padx=10, pady=10)
            k += 1
