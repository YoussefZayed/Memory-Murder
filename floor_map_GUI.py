from tkinter import *
from PIL import Image, ImageTk
import time

window = Tk()
window.geometry("1000x775")
window.config(bg="white")
window.resizable(0,0)
image = Image.open("floor_plan.png")
floor_map = ImageTk.PhotoImage(image.resize((750, 775), Image.ANTIALIAS))


label = Label(window, image=floor_map)
label.photo = floor_map
label.pack(side=LEFT)

date_var = IntVar()
date_format = StringVar()
date_format.set(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(date_var.get())))

timeline = Scale(window, from_=1578151801, to=1578236760, variable=date_var, orient=HORIZONTAL, length=200).pack()
date_label = Label(window, textvariable=date_format).pack()



class ButtonObject:
    def __init__(self, x, y):
        self.state = BooleanVar()
        self.button = Button(window, bg="red", command=self.switch)
        self.button.place(x=x, y=y, height=10, width=10, in_=window)

    def switch(self):
        self.state = not self.state
        self.check_state()

    def check_state(self):
        if self.state:
            self.button.config(bg="green")
        else:
            self.button.config(bg="red")
        self.button.after(1, self.check_state)


con_room = ButtonObject(245, 155)

while True:
    date_format.set(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(date_var.get())))

    try:
        window.update()
    except:
        exit(0)

