from tkinter import *
import random
import ast

root = Tk()
root.title("Рандомайзер")
canvas = Canvas(root, height=600, width=1200, bg="grey")
canvas.pack()

examples = {}
with open('examples.txt') as examples_file:
    examples_text = examples_file.read()
examples = dict(ast.literal_eval(examples_text))


def resetBoard():
    global final_respon
    button.pack_forget()
    button2.pack_forget()
    line_generator()
    main()


def line_generator():
    global final_respon
    respon1 = random.choice(examples["первое"])
    respon2 = random.choice(examples["второе"])
    respon3 = random.choice(examples["третье"])
    respon4 = random.choice(examples["четвертое"])
    final_respon = "%s %s %s %s" % (respon1, respon2, respon3, respon4)


def main():
    global button
    global button2
    canvas.delete('all')
    button = Button(root, text="Еще", command=resetBoard)
    button.pack()
    button2 = Button(root, text="Выход", command=exit)
    button2.pack()
    line_generator()
    canvas.create_text(600, 200, text=final_respon, font="Georgia 22", fill="black")
    canvas.update()


main()

root.mainloop()
