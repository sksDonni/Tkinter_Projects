from tkinter import *
import io


class PrintAlphabet:

    def __init__(self, root):
        self.root = root

    def show_alphabet(self, root, frame, filename):
        self.root = root
        i = 0
        k = 0
        j = 0
        text = ""

        with io.open(filename, "r", encoding="utf-8") as f:
            text = f.read()
        alphabets = []
        for te in text:
            if te == "":
                continue
            alphabets.append(te)

        for j in range(0, len(text)):
            if text[j].encode("utf-8") == "が".encode("utf-8") or text[j].encode("utf-8") == "ガ".encode("utf-8"):
                for i in range(0, 10):
                    dashes = Label(frame, text="||")
                    dashes.grid(row=i, column=5)

                temp = j
                w = 0
                k = 6
                for j in range(temp, len(text)):
                    if j % 5 == 0:
                        w += 1
                        k = 6
                    label = Label(frame, text=text[j], font="Helvetica 24 bold")
                    label.grid(row=w, column=k, padx=10, pady=10)
                    k += 1
                break

            if j % 5 == 0 and j != 0:
                i += 1
                k = 0
            label = Label(frame, text=text[j], font="Helvetica 24 bold")
            label.grid(row=i, column=k, padx=10, pady=10)
            k += 1

        frame.tkraise()