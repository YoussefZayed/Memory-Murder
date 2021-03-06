from tkinter import *
from PIL import Image, ImageTk
import time
from databaseBuilder import *

# Epoch time constants
START_TIME = 1578151801
END_TIME = 1578236760

names = ["Veronica", "Jason", "Thomas", "Rob", "Kristina", "Marc-Andre", "Dave", "Salina", "Harrison", "Alok", "Eugene"]

window = Tk()
window.title("Richcraft Hotel (Formerly Known as the River Building)")
window.geometry("1250x800")
window.resizable(0, 0)

image = Image.open("floor_plan.png")
floor_map = ImageTk.PhotoImage(image.resize((750, 775), Image.ANTIALIAS))


def show(event):
    print(event.x, event.y)
map_label = Label(window, image=floor_map)
map_label.photo = floor_map
map_label.pack(side=LEFT)
map_label.bind("<B1-Motion>", show)

# Date Slider and Epoch-local conversion
date_var = IntVar()

date_format = StringVar()

slider_frame = Frame(window)
# Timeline Slider
timeline = Scale(slider_frame, from_=START_TIME, to=END_TIME, variable=date_var, orient=VERTICAL, length=700,
                 font=("Courier", 10)).grid(row=0)
date_label = Label(slider_frame, textvariable=date_format, font=("Courier", 10)).grid(row=1)
slider_frame.pack(side=LEFT)


check_frame = Frame(window, height=500, borderwidth=5, relief="groove", pady=10)

check_vars = []
checkbuttons = []
for x in range(0, 11):
    check_vars += [IntVar()]
    c = Checkbutton(check_frame, text=names[x], variable=check_vars[x]) 
    checkbuttons += [c]
    c.grid(pady = 10)
check_frame.pack()

effect_pause_var = IntVar()
effect_pause_button = Checkbutton(window, text="Pause for Important Moments", font=("Courier", 10), variable=effect_pause_var)
effect_pause_button.pack()

run_frame = Frame(window)
run_speed = IntVar()
lab = Label(run_frame, text="Run Speed").pack(side=LEFT)
runtime = Scale(run_frame, from_=1, to=20, variable=run_speed, orient=HORIZONTAL, length=170,
                 font=("Courier", 10)).pack(side=RIGHT)
run_frame.pack()

# button object to create toggle buttons
class ButtonObject:
    def __init__(self, x, y, text=None, h=15, w=15):
        self.state = BooleanVar()
        self.button = Button(window, bg="red", command=self.switch, text=text)
        self.button.place(x=x, y=y, height=h, width=w, in_=window)
        self.color = "red"

    def switch(self):  # Switch button state
        self.check_state()
        self.state = not self.state

    def check_state(self):  # Changes colour based on button state
        if self.state:
            self.button.config(bg="green")
        else:
            self.button.config(bg="red")
    def invoke(self):
        if self.color == "red":
            self.color = "green"
        else:
            self.color = "red"
        self.button.invoke()


# people object to create people tags
class Person:
    def __init__(self, name, room, x=None, y=None):
        self.state = BooleanVar()
        self.has_label = False
        if room is not None:
            x, y = room_pos[room][0], room_pos[room][1]
        self.x, self.y = x, y
        self.connection = None
        self.room = None
        for (k, n) in room_pos.items():  # Find person's room based on pixel coordinates
            if (self.x, self.y) == n:
                if type(k) == int:
                    self.room = k
                else:
                    self.connection = k
        self.name = name
        self.sensor = None
        self.button = Button(window, bg="Blue", command=self.switch, text=name[0])
        self.button.place(x=x, y=y, height=20, width=20, in_=window)

    def switch(self):  # Switch button state
        self.display()
        self.state = not self.state

    def display(self):  # Creates a label displaying object's variables
        if self.state:
            self.has_label = True
            text = "Name: " + self.name + "\nRoom: " + str(self.room) + "\nWi-Fi: " + str(
                self.connection) + "\nTriggered: " + str(self.sensor)
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
        if type(new_room) == int:
            self.room = new_room
        else:
            self.room = None
            self.connection = new_room

    def set_triggered(self, area):
        self.sensor = area


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
    "elevator": (349, 633),
    "ice machine": (345, 711),
    "stairwell": (700, 590)
}

ap_pos = {
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
    101: (490, 112),
    110: (175, 180),
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
    248: (600, 680),
    "ap1-1": (180, 245),
    "ap1-2": (510, 256),
    "ap1-3": (380, 360),
    "ap1-4": (340, 190),
    "ap2-1": (245, 590),
    "ap2-2": (550, 590),
    "ap2-3": (425, 590)
}
# Most rooms have doors and phones
phone_pos = door_pos.copy()

phone_pos["lobby"] =  (344, 160)

# Turn coordinates in dict to toggle buttons
for key in door_pos:

    door_pos[key] = ButtonObject(door_pos[key][0], door_pos[key][1], "D")

for key in phone_pos:
    phone_pos[key] = ButtonObject(phone_pos[key][0] - 15, phone_pos[key][1], "P")

for key in motion_pos:
    motion_pos[key] = ButtonObject(motion_pos[key][0], motion_pos[key][1], "M")
for key in ap_pos:
    ap_pos[key] = ButtonObject(ap_pos[key][0], ap_pos[key][1], "W")

people = {}
for x in names:
    people[x[0]] = Person(x, None, 2000, 2000)

# Creates the play toggle button
play_button = ButtonObject(835, 770, "Play", 20, 30)

# update GUI elements
# Interfacing with database should probably be done in here, as positions and data
# can be updated

def reset():
    for key in door_pos:
        if phone_pos[key].color == "green":
            phone_pos[key].invoke()
        if door_pos[key].color == "green":
            door_pos[key].invoke()
    for key in motion_pos:
        if motion_pos[key].color == "green":
            motion_pos[key].invoke()
    for key in ap_pos:
        if ap_pos[key].color == "green":
            ap_pos[key].invoke()



def trigger_event(database,current_time):
    """ updates all elements to where they should be right now on  the time line """
    background_data = database.dataReturnIf(['time'],[[START_TIME,current_time]],0,"Murder")
    reset()
    for event in background_data:
        if event[1] == "door sensor":
            door_num = event[2]
            if event[2] == "156b":
                door_num = 156.5
            door = door_pos[int(door_num)]
            if door.color == "green" and event[3] == "door closed":
                door.invoke()
            if door.color == "red" and ( event[3] == "unlocked no keycard" or event[3] == "successful keycard unlock") :
                door.invoke()
                if event[4] != "n/a":
                    people[event[4][0]].move(int(door_num))
                    people[event[4][0]].set_triggered(door_num)
        elif event[1] == "phone":
            pass

        if event[1] == "access point":
            ap = event[2]
            if event[4] != "n/a":
                people[event[4][0]].move(ap)
        if event[1] == "phone":
            phone_num = event[2]
            if phone_num == "reception":
                phone_num = 101
            if phone_num != "lobby":
                phone_num = int(phone_num)
            phone = phone_pos[(phone_num)]
            if phone.color == "green" and event[3] == "off hook":
                phone.invoke()
            if phone.color == "red" and (event[3] == "on hook"):
                phone.invoke()

        elif event[1] == "motion sensor":
            motion_pos[event[2]].invoke()
            if event[4] != "n/a":
                people[event[4][0]].set_triggered(event[2])

        if event[4] != "n/a" and check_vars[names.index(event[4])].get(): 
            people[event[4][0]].move(None, 2000, 2000)
    if database.dataReturnIf(["time"],[[current_time]],0,"Murder") and effect_pause_var.get():
        play_button.invoke()

previous_time = date_var.get()
date_format.set(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(date_var.get())))

while True:
    # Updates the date & time tag and converts from epoch time
    current_time = date_var.get()
    if current_time != previous_time:
        date_format.set(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(date_var.get())))
        database = DatabaseBuilder("data.db","Murder")
        trigger_event(database,date_var.get())
    previous_time = date_var.get()
    # Scrubs through timeline when play button is toggled
    if not play_button.state:
        date_var.set(date_var.get() + run_speed.get())

    try:
        
        window.update()  # Update the GUI elements
    except:
        exit(0)
