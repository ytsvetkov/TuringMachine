from tkinter import *


def draw_curve(x, a):
    '''Draws the so called "Witch of Agnesi" curve.'''
    return (8 * a * a * a) / (x * x + 4 * a * a)


def draw_arrow(i, j, canvas):
    x1 = (10 + 80 * i) + 15
    x2 = (10 + 80 * j)
    diff = (x2 + x1 + 15) / 2
    if i == j:
        canvas.create_oval(x2, 390 - 10, x1 + 5 + 5, 410)
        canvas.create_line(x1 - 5 + 7, 400, x1 + 7, 405, width=2, fill="black")
        canvas.create_line(x1 + 5 + 7, 400, x1 + 7, 405, width=2, fill="black")
        return
    elif i + 1 == j:
        canvas.create_line(x1, 405, x2, 405, width=2, fill="green")
        canvas.create_line(x2 - 5, 400, x2, 405, width=2, fill="green")
        canvas.create_line(x2 - 5, 410, x2, 405, width=2, fill="green")
        return
    elif j + 1 == i:
        canvas.create_line(x1, 405, x2, 405, width=2, fill="green")
        canvas.create_line(x1, 405, x2 - 5, 400, width=2, fill="green")
        canvas.create_line(x1, 405, x2 - 5, 410, width=2, fill="green")
        return
    while x1 <= x2 + 15:
        canvas.create_line(
            x1, draw_curve(x1 - diff, (abs(i - j)) * 5 + 10) + 400, x1 + 3,
            draw_curve(x1 + 3 - diff, (abs(i - j)) * 5 + 10) + 400,
            width=2, fill="blue")
        x1 += 3


def draw_automata(turing_machine):

    master = Tk()
    canvas = Canvas(master, width=800, height=800)

    master.protocol("WM_DELETE_WINDOW", master.quit())
    Button(master, text='Quit', command=master.quit).pack(
        side=BOTTOM, anchor=SE)
    canvas.pack()

    for i in range(len(turing_machine.states)):
        canvas_id = canvas.create_text(10 + 80 * i, 400, anchor="nw")
        canvas.itemconfig(canvas_id, text="state-")
        canvas.insert(canvas_id, 12, "%d" % i)

    for rule in turing_machine.rules:
        draw_arrow(rule.current_state, rule.next_state, canvas)

    master.mainloop()
