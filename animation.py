from tkinter import *
import time
from math import cos, sin, pi

class alien:

    def __init__(self, machine=None):
        self.root = Tk()
        self.canvas = Canvas(self.root, width=800, height=400)
        self.canvas.pack()
        self.machine = machine
        self.root.after(0, self.animation)
        self.root.mainloop()
        self.canvas.create_line(10, 10, 100, 100, width=2, fill='black')

    def draw_tape(self):
        length = 35 * \
            (len(self.machine.tape.left) + 1 + len(self.machine.tape.right))

        self.canvas.create_line(10, 175+100, 760, 175+100, width=2, fill='black')
        self.canvas.create_line(760, 175+100, 760, 225+100, width=2, fill='black')
        self.canvas.create_line(760, 225+100, 10, 225+100, width=2, fill='black')
        self.canvas.create_line(10, 225+100, 10, 175+100, width=2, fill='black')


        preprocessed_text = self.machine.tape.right
        preprocessed_text.appendleft(self.machine.tape.middle)
        text = self.machine.tape.left
        text.extend(preprocessed_text)


        cell_length = 750 // (length // 35)
        for i in range(length // 35):
            self.canvas.create_line(10 + i * cell_length, 175+100, 10 + i * cell_length, 225+100,
                                    width=2, fill='black')
            canvas_id = self.canvas.create_text(10 + i * cell_length, 175+100, font=("Default",30), anchor="nw")
            self.canvas.itemconfig(canvas_id)
            self.canvas.insert(canvas_id,12, "%c" % text[i])
  

        deg = 45
        leng = 150
        self.canvas.create_line(10+8.5*cell_length, 175+100, 10+8.5*cell_length+sin(2*pi/360*deg)*leng,175+100 - cos(2*pi/360*deg)*leng, width=2, fill='black')
        self.canvas.create_line(10+8.5*cell_length, 175+100, 10+8.5*cell_length-sin(2*pi/360*deg)*leng,175+100 - cos(2*pi/360*deg)*leng, width=2, fill='black')
        self.canvas.create_line(10+8.5*cell_length+sin(2*pi/360*deg)*leng,175+100 - cos(2*pi/360*deg)*leng, 10+8.5*cell_length-sin(2*pi/360*deg)*leng,175+100 - cos(2*pi/360*deg)*leng, width=2, fill='black')
        third = (10+8.5*cell_length+sin(2*pi/360*deg)*leng)/3
        self.canvas.create_line(10+8.5*cell_length+30, 175+100 - cos(2*pi/360*deg)*leng,10+8.5*cell_length+30, 10, width=2, fill='black')
        self.canvas.create_line(10+8.5*cell_length-30, 175+100 - cos(2*pi/360*deg)*leng,10+8.5*cell_length-30, 10, width=2, fill='black')
        self.canvas.create_line(10+8.5*cell_length-30, 10,10+8.5*cell_length+30, 10, width=2, fill='black')
        
        return

    def animation(self):
        self.draw_tape()
