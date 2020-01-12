from tkinter import *
from PIL import Image, ImageTk
import time

# Epoch time constants
START_TIME = 1578151801
END_TIME = 1578236760

window = Tk()
window.geometry("1200x800")
window.resizable(0, 0)
image = Image.open("floor_plan.png")
floor_map = ImageTk.PhotoImage(image.resize((750, 775), Image.ANTIALIAS))

map_label = Label(window, image=floor_map)
map_label.photo = floor_map
map_label.pack(side=LEFT)

# Date Slider and Epoch-local conversion
date_var = IntVar()
date_format = StringVar()

# Timeline Slider
timeline = Scale(window, from_=START_TIME, to=END_TIME, variable=date_var, orient=VERTICAL, length=700,
                 font=("Courier", 10)).pack(side=LEFT)
date_label = Label(window, textvariable=date_format, font=("Courier", 10)).pack(side=LEFT)


# This stuff is for the text input
# def get_time():
#     new_time = time_input.get()
#     print(new_time)
#     epoch_time = int(time.mktime(time.strptime("20" + new_time, "%Y.%m.%d %HH:%MM:%SS")))
#     print(epoch_time)
#
# input_label = Label(window, text="Input a desired time (HH:MM:SS)").pack()
# time_input = Entry(window)
# time_button = Button(window, text="Set", command=get_time)
#
# time_input.pack()
# time_button.pack()


# button object to create toggle buttons
class ButtonObject:
    def __init__(self, x, y, text=None, h=15, w=15):
        self.state = BooleanVar()
        self.button = Button(window, bg="red", command=self.switch, text=text)
        self.button.place(x=x, y=y, height=h, width=w, in_=window)

    def switch(self):  # Switch button state
        self.check_state()
        self.state = not self.state

    def check_state(self):  # Changes colour based on button state
        if self.state:
            self.button.config(bg="green")
        else:
            self.button.config(bg="red")


# people object to create people tags
class Person:
    def __init__(self, name, x, y):
        self.state = BooleanVar()
        self.has_label = False
        self.x, self.y = x, y
        for (k, n) in room_pos.items():  # Find person's room based on pixel coordinates
            if (self.x, self.y) == n:
                self.room = k
        self.name = name
        self.button = Button(window, bg="Blue", command=self.switch, text=name[0])
        self.button.place(x=x, y=y, height=20, width=20, in_=window)

    def switch(self):  # Switch button state
        self.display(self.name, self.room, "AP1-1", "M-210")
        self.state = not self.state

    def display(self, name, room, connection, sensor):  # Creates a label displaying object's variables
        if self.state:
            self.has_label = True
            text = "Name: " + name + "\nRoom: " + str(room) + "\nWi-Fi: " + connection + "\nTriggered: " + sensor
            self.display_label = Label(window, text=text, font=('Courier', 7))
            self.display_label.place(x=self.x, y=self.y - 55, in_=window)
        else:
            self.display_label.destroy()

    def move(self, new_room=None, new_x=None, new_y=None):  # Moves person to a different pixel coord or room
        if new_room is not None:
            new_x, new_y = room_pos[new_room][0], room_pos[new_room][1]
        self.button.place(x=new_x, y=new_y, in_=window)
        if self.has_label:
            if self.display_label.winfo_exists():
                self.display_label.place(x=new_x, y=new_y - 55, in_=window)
        self.x, self.y = new_x, new_y
        self.room = new_room


# oh no oh god please don't look
door_pos = {
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

# I'm so, so sorry
room_pos = {
    110: (175, 180),
    101: (490, 112),
    151: (490, 170),
    155: (596, 170),
    130: (175, 355),
    152: (472, 355),
    154: (546, 355),
    156: (615, 330),
    156.5: (615, 375),
    210: (165, 475),
    231: (250, 485),
    233: (345, 485),
    235: (425, 485),
    241: (515, 485),
    247: (605, 485),
    220: (165, 666),
    232: (250, 700),
    236: (435, 700),
    244: (517, 680),
    248: (600, 680)

}
# Most rooms have doors and phones
phone_pos = door_pos.copy()

# Turn coordinates in dict to toggle buttons
for key in door_pos:
    phone_pos[key] = ButtonObject(door_pos[key][0] - 15, door_pos[key][1], "P")
    door_pos[key] = ButtonObject(door_pos[key][0], door_pos[key][1], "D")

for key in motion_pos:
    motion_pos[key] = ButtonObject(motion_pos[key][0], motion_pos[key][1], "M")
for key in hotspot_pos:
    hotspot_pos[key] = ButtonObject(hotspot_pos[key][0], hotspot_pos[key][1], "W")

# Test People
Thomas = Person("Thomas", room_pos[110][0], room_pos[110][1])
Thomette = Person("Screem", room_pos[156][0], room_pos[156][1])

# Creates the play toggle button
play_button = ButtonObject(835, 745, "Play", 20, 30)

# update GUI elements
# Interfacing with database should probably be done in here, as positions and data
# can be updated
while True:
    # Updates the date & time tag and converts from epoch time
    date_format.set(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(date_var.get())))

    #Scrubs through timeline when play button is toggled
    if not play_button.state:
        date_var.set(date_var.get() + 5)

    if date_var.get() == START_TIME + 5:
        Thomas.move(236) #Move person to room key
        Thomette.move(None, 250, 300) #Move person to pixel coord
    try:
        window.update() #Update the GUI elements
    except:
        exit(0)
