from tkinter import *
from PIL import Image, ImageTk
import time

# Epoch time constants
START_TIME = 1578151801
END_TIME = 1578236760

window = Tk()
window.geometry("1000x775")
window.resizable(0, 0)
image = Image.open("floor_plan.png")
floor_map = ImageTk.PhotoImage(image.resize((750, 775), Image.ANTIALIAS))


def mouse(event):
    print(event.x, event.y)


# Map Frame
label = Label(window, image=floor_map)
label.photo = floor_map
label.pack(side=LEFT)
label.bind("<B1-Motion>", mouse)

# Date Slider and Epoch-local conversion
date_var = IntVar()
date_format = StringVar()
date_format.set(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(date_var.get())))

timeline = Scale(window, from_=START_TIME, to=END_TIME, variable=date_var, orient=VERTICAL, length=700,
                 font=("Courier", 10)).pack()
date_label = Label(window, textvariable=date_format, font=("Courier", 10)).pack()


# button object to create toggle buttons
class ButtonObject:
    def __init__(self, x, y, text=None, h=15, w=15):
        self.state = BooleanVar()
        self.button = Button(window, bg="red", command=self.switch, text=text)
        self.button.place(x=x, y=y, height=h, width=w, in_=window)

    def switch(self):
        self.check_state()
        self.state = not self.state

    def check_state(self):
        if self.state:
            self.button.config(bg="green")
        else:
            self.button.config(bg="red")


class Person:
    def __init__(self, name, x, y):
        self.state = BooleanVar()
        self.x, self.y = x, y
        self.button = Button(window, bg="Blue", command=self.switch, text=name)
        self.button.place(x=x, y=y, height=20, width=20, in_=window)

    def switch(self):
        self.display("Thomas", 210, "AP1-1", "M-210")
        self.state = not self.state

    def display(self, name, room, connection, sensor):
        if self.state:
            text = "Name: " + name + "\nRoom: " + str(room) + "\nWi-Fi: " + connection + "\nTriggered: " + sensor
            self.display_label = Label(window, text=text, font=('Courier', 7))
            self.display_label.place(x=self.x, y=self.y-55, in_=window)
        else:
            self.display_label.destroy()

    def move(self, new_room=None, new_x=None, new_y=None):
        self.button.place(x=new_x, y=new_y, in_=window)
        if self.display_label.winfo_exists():
            self.display_label.place(x=new_x, y=new_y-55, in_=window)
        self.x, self.y = new_x, new_y


# oh no don't look
room_pos = {
    101: (445, 117),
    110: (245, 155),
    151: (496, 210),
    155: (605, 210),
    130: (245, 371),
    156: (622, 295),
    156.5: (622, 356),
    150: (655, 242),
    210: (212, 570),
    231: (258, 523),
    233: (340, 523),
    235: (433, 523),
    241: (522, 548),
    247: (605, 548),
    220: (211, 622),
    232: (254, 659),
    236: (438, 660),
    244: (525, 634),
    248: (612, 634),
    250: (655, 620)
}

motion_pos = {
    200: (349, 633),
    234: (345, 711),
    150: (700, 250),
    250: (700, 590)
}

hotspot_pos = {
    11: (180, 150),
    12: (553, 250),
    13: (345, 360),
    14: (344, 160),
    21: (250, 580),
    22: (555, 580),
    23: (433, 580)
}

door_pos = room_pos.copy()
phone_pos = room_pos.copy()

# Turn coorinates in dict to toggle buttons
for key in room_pos:
    door_pos[key] = ButtonObject(room_pos[key][0], room_pos[key][1], "D")
    phone_pos[key] = ButtonObject(room_pos[key][0] - 15, room_pos[key][1], "P")
for key in motion_pos:
    motion_pos[key] = ButtonObject(motion_pos[key][0], motion_pos[key][1], "M")
for key in hotspot_pos:
    hotspot_pos[key] = ButtonObject(hotspot_pos[key][0], hotspot_pos[key][1], "W")

Thomas = Person("T", 166, 100)

play_button = ButtonObject(870, 745, "Play", 20, 30)
# update GUI elements
while True:
    date_format.set(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(date_var.get())))
    if not play_button.state:
        date_var.set(date_var.get() + 5)

    if date_var.get() == START_TIME + 5:
        Thomas.move(None, 500, 500)
    try:
        window.update()
    except:
        exit(0)
