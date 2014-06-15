from tkinter import Tk, Canvas, PhotoImage, Label, Button, DISABLED
import time
from math import cos, sin, pi


class Animate:

    def __init__(self, machine=None):
        self.machine = machine
        self.symbol = [1]*17
        self.text_rule = ''

        self.root = Tk()
        self.canvas = Canvas(self.root, width=800, height=400)
        self.step_button = Button(self.root, text="Step",
                                    command=self.step)
        self.step_button.pack()
        self.animate_button = Button(self.root, text="Animate",
                                    command=self.animate)
        self.animate_button.pack()
        self.canvas.pack()

        self.initialise_window()
        self.root.mainloop()

    def initialise_window(self):

        self.canvas.create_rectangle(10,275, 760, 325, width=2)
        self.canvas.create_rectangle(10,275, 760, 325, width=2)
        for i in range(17):
            self.canvas.create_line(10 + i*44, 275, 10 + i * 44, 325, width=2)
        deg = 45
        leng = 150
        self.canvas.create_line(384, 275, 384+sin(2*pi/360*deg)*leng,
                                275 - cos(2*pi/360*deg)*leng, width=2)
        self.canvas.create_line(384, 275, 384-sin(2*pi/360*deg)*leng,
                                275 - cos(2*pi/360*deg)*leng, width=2)
        self.canvas.create_line(384+sin(2*pi/360*deg)*leng,
                                275 - cos(2*pi/360*deg)*leng,
                                384-sin(2*pi/360*deg)*leng,
                                275 - cos(2*pi/360*deg)*leng, width=2)
        self.canvas.create_line(414, 275 - cos(2*pi/360*deg)*leng,
                                414, 10, width=2)
        self.canvas.create_line(354, 275 - cos(2*pi/360*deg)*leng,
                                354, 10, width=2)
        self.canvas.create_line(354, 10, 414, 10, width=2)
        self.canvas.pack()

    def animate(self):
        while (self.machine.current_state not in self.machine.accept_states) and\
                (self.machine.current_state not in self.machine.reject_states):
            self.step()
            time.sleep(0.7)
        self.finalise()

    def step(self):
        if self.machine.current_state in self.machine.accept_states:
            self.finalise()
        elif self.machine.current_state in self.machine.reject_states:
            self.finalise()

        self.canvas.update()
        left_from_head = ''
        right_from_head = ''
        head = str(self.machine.tape.middle)
        for i in self.machine.tape.right:
            right_from_head += str(i)
        for i in self.machine.tape.left:
            left_from_head += str(i)
        if len(right_from_head) > 8:
            right_from_head = right_from_head[:8]
        elif len(right_from_head) < 8:
            right_from_head = right_from_head + '_'*(8 - len(right_from_head))
        if len(left_from_head) > 8:
            left_from_head = left_from_head[-8:]
        elif len(left_from_head) < 8:
            left_from_head = '_'*(8 - len(left_from_head)) + left_from_head
        text = left_from_head + head + right_from_head
        for i in range(17):
            if self.symbol[i]:
                self.canvas.delete(self.symbol[i])
            self.symbol[i] = self.canvas.create_text(10 + i * 44, 275,
                                                    text="%c" % text[i],
                                                    font=("Default", 30),
                                                    anchor="nw")

        rule = self.machine.step()
        if rule is None:
            self.finalise()
        self.canvas.delete(self.text_rule)
        self.text_rule = self.canvas.create_text(54 + 374-sin(pi/4)*150,
                                                275 - cos(pi/4)*150,
                                                text="%s" % rule,
                                                font=("Default", 12),
                                                anchor="nw")

    def finalise(self):
        mesg = self.canvas.create_text(0, 0, font=("Default", 30), anchor="nw")
        self.canvas.itemconfig(mesg)
        if self.machine.current_state in self.machine.accept_states:
            self.canvas.insert(mesg, 12, "%s" % 'Accept !!!')
            photo = PhotoImage(file="img/HappyTuring.gif")
            label = Label(image=photo)
            label.pack()
            self.root.mainloop()
        elif self.machine.current_state in self.machine.reject_states:
            self.canvas.insert(mesg, 12, "%s" % 'Reject !!!')
            photo = PhotoImage(file="img/SadTuring.gif")
            label = Label(image=photo)
            label.pack()
            self.root.mainloop()
        else:
            self.canvas.insert(mesg, 12, "%s" % 'Halt !!!')
            photo = PhotoImage(file="img/ConfusedTuring.gif")
            label = Label(image=photo)
            label.pack()
            self.root.mainloop()