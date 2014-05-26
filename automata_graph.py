from tkinter import *


state_position = {}


def draw_arrow(i, j, canvas, counter):
    if i == j:
        canvas.create_oval(10 + 80 * j, 390 - 10, 10 + 80 * i + 20 + 5, 410)
        canvas.create_line(10 + 80 * i - 5 + 25, 400, 10 + 80 *
                           i + 25, 405, width=2, fill="black")
        canvas.create_line(10 + 80 * i + 5 + 25, 400, 10 + 80 * i +
                           25, 405, width=2, fill="black")

    else:
        canvas.create_line(10 + 80 * i, 400, 10 + 80 * i, i + (-10)
                           * counter + 400, width=1, fill='blue')
        canvas.create_line(10 + 80 * i, i + (-10) * counter + 400,
                           10 + 80 * j+35, i + (-10) * counter + 400,
                           width=1, fill='blue')
        canvas.create_line(10 + 80 * j+35, i + (-10) * counter + 400,
                           10 + 80 * j+35, 400, width=1, fill='blue')
    return counter + 1


def draw_automata(turing_machine=None):

    master = Tk()
    canvas = Canvas(master, width=800, height=800)

    master.protocol("WM_DELETE_WINDOW", master.quit())
    Button(master, text='Quit', command=master.quit).pack(
        side=BOTTOM, anchor=SE)
    canvas.pack()

    for position, state in enumerate(turing_machine.states):
        state_position[state] = position
        canvas_id = canvas.create_text(10 + 80 * position, 400, anchor="nw")
        canvas.itemconfig(canvas_id, text="state-")
        canvas.insert(canvas_id, 12, "%d" % state)

    counter = 1
    for rule in turing_machine.rules:
        counter = draw_arrow(state_position[rule.current_state],
                             state_position[rule.next_state], canvas, counter)

    master.mainloop()
