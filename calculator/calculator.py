from tkinter import *

root = Tk()
root.title("simple calculator")

text_to_be_evaluated = StringVar()
text_to_be_evaluated.set("")
myentry = Entry(root, textvar=text_to_be_evaluated, width=30, borderwidth=10)
myentry.grid(row=0, column=0, columnspan=3, padx=10, pady=5)
mytext = ""


# defining methods
def number_operation(i):
    global mytext
    global ans
    if i == "=":
        try:
            ans = eval(mytext)
            text_to_be_evaluated.set(ans)
            myentry.update()
            mytext = ""

        
        except Exception as e:
            print(e)
            text_to_be_evaluated.set("Error")
            myentry.update()
            mytext = ""

    elif i == "C":
        mytext = ""
        text_to_be_evaluated.set("")

    elif i == "Ans":
        mytext += str(ans)
        text_to_be_evaluated.set(mytext)
        myentry.update()

    elif i == "sqrt":
        try:
            print(mytext)
            if mytext.isdigit():
                ans = int(mytext) ** 0.5
                text_to_be_evaluated.set(ans)
                myentry.update()
                mytext = ""

        except Exception as e:
            print(e)
            mytext = ""

    else:
        mytext += str(i)
        text_to_be_evaluated.set(mytext)
        myentry.update()


# initializing buttons
button_0 = Button(root, text="0", padx=5, pady=5, width=10, command=lambda: number_operation(0))

button_1 = Button(root, text="1", padx=5, pady=5, width=10, command=lambda: number_operation(1))
button_2 = Button(root, text="2", padx=5, pady=5, width=10, command=lambda: number_operation(2))
button_3 = Button(root, text="3", padx=5, pady=5, width=10, command=lambda: number_operation(3))

button_4 = Button(root, text="4", padx=5, pady=5, width=10, command=lambda: number_operation(4))
button_5 = Button(root, text="5", padx=5, pady=5, width=10, command=lambda: number_operation(5))
button_6 = Button(root, text="6", padx=5, pady=5, width=10, command=lambda: number_operation(6))

button_7 = Button(root, text="7", padx=5, pady=5, width=10, command=lambda: number_operation(7))
button_8 = Button(root, text="8", padx=5, pady=5, width=10, command=lambda: number_operation(8))
button_9 = Button(root, text="9", padx=5, pady=5, width=10, command=lambda: number_operation(9))

button_clear = Button(root, text="clear", padx=5, pady=5, width=23, command=lambda: number_operation("C"))
button_equals = Button(root, text="=", padx=5, pady=5, width=23, command=lambda: number_operation("="))

button_add = Button(root, text="+", padx=5, pady=5, width=10, command=lambda: number_operation("+"))
button_sub = Button(root, text="-", padx=5, pady=5, width=10, command=lambda: number_operation("-"))
button_mul = Button(root, text="*", padx=5, pady=5, width=10, command=lambda: number_operation("*"))
button_div = Button(root, text="/", padx=5, pady=5, width=10, command=lambda: number_operation("/"))
button_squareroot = Button(root, text="sqroot", padx=5, pady=5, width=10, command=lambda: number_operation("sqrt"))
button_prev_answer = Button(root, text="Ans", padx=5, pady=5, width=10, command=lambda: number_operation("Ans"))

# adding buttons on to the root screen

button_0.grid(row=4, column=0)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_add.grid(row=5, column=0)
button_sub.grid(row=1, column=3)
button_mul.grid(row=2, column=3)
button_div.grid(row=3, column=3)
button_squareroot.grid(row=4, column=1)
button_prev_answer.grid(row=5, column=1)

button_clear.grid(row=4, column=2, columnspan=2)
button_equals.grid(row=5, column=2, columnspan=2)


if __name__ == '__main__':
    root.mainloop()
