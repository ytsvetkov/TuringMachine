from tkinter import *


state_position = {}


def draw_arrow(i, j, canvas, counter, rule):
    if i == j:
        canvas.create_oval(10 + 80 * i, 410, 10 + 80 * i + 20 + 5, 440)
        canvas_id = canvas.create_text(10 + 80 * i, 445, anchor="nw")
        canvas.itemconfig(canvas_id, text="%s" % rule)
        canvas.insert(canvas_id, 12, "")
    else:
        canvas.create_line(10 + 80 * i, 400, 10 + 80 * i, i + (-10)
                           * counter * 1.7 + 400, width=1, fill='blue')
        canvas.create_line(10 + 80 * i, i + (-10) * counter * 1.7 + 400,
                           10 + 80 * j + 35, i + (-10) * counter * 1.7 + 400,
                           width=1, fill='blue')
        canvas.create_line(10 + 80 * j + 35, i + (-10) * counter * 1.7 + 400,
                           10 + 80 * j + 35, 400, width=1, fill='blue')
        canvas.create_line(10 + 80 * j + 30, 395, 10 + 80 *
                           j + 35, 400, width=1, fill='blue')
        canvas.create_line(10 + 80 * j + 40, 395, 10 + 80 *
                           j + 35, 400, width=1, fill='blue')

    if i < j:
        canvas_id = canvas.create_text(
            10 + 80 * i, i + (-10) * counter * 1.7 + 385, anchor="nw")
        canvas.itemconfig(canvas_id, text="%s" % rule)
        canvas.insert(canvas_id, 12, "")
    elif i > j:
        canvas_id = canvas.create_text(
            10 + 80 * i - 100, i + (-10) * counter * 1.7 + 385, anchor="nw")
        canvas.itemconfig(canvas_id, text="%s" % rule)
        canvas.insert(canvas_id, 12, "")

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
                             state_position[rule.next_state],
                             canvas, counter, rule)

    master.mainloop()
