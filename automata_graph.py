from tkinter import *


master = Tk()
w = Canvas(master, width=800, height=800)
w.pack()


for i in range(10):
    for j in range(5):
        canvas_id = w.create_text(10 + 80 * i, 10 + 80 * j, anchor="nw")
        w.itemconfig(canvas_id, text="t")
        w.insert(canvas_id, 12, "new")

# the line
w.create_line(10 + 80 + 10, 10 + 80 + 5, 10 + 240 + 10, 10 + 240 + 5)
# the text
canvas_id = w.create_text(180, 175, anchor="nw")
w.itemconfig(canvas_id, text="a")
w.insert(canvas_id, 12, "b")
# arrow
w.create_line(10 + 240, 10 + 240, 10 + 240 + 10, 10 + 240 + 5)
w.create_line(10 + 240 + 4.5, 10 + 240 - 5.5, 10 + 240 + 10, 10 + 240 + 5)


master.mainloop()
