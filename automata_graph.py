from tkinter import *


state_position = {}
loop_occurrences = {}


def draw_arrow(i, j, canvas, counter, rule):
    if i == j:
        canvas.create_oval(10 + 80 * i, 410, 10 + 80 * i + 20 + 5, 440)
        canvas_id = canvas.create_text(
            10 + 80 * i - 10, 445 + 30 * loop_occurrences[i], anchor="nw", font=("Default", 9))
        loop_occurrences[i] += 1
        message = str(rule)[1:-2].split(")(")
        canvas.itemconfig(canvas_id, text="%s" %
                          message[0] + ')-⌄\n(' + message[1] + ')')
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

    w = len(turing_machine.states)
    h = len(turing_machine.rules)

    root = Tk()
    frame = Frame(root, width=800, height=600)
    frame.grid(row=0, column=0)
    canvas = Canvas(frame, bg='#FFFFFF', width=800, height=600,
                    scrollregion=(0, -h * 15, w * 100, h * 15))
    hbar = Scrollbar(frame, orient=HORIZONTAL)
    hbar.pack(side=BOTTOM, fill=X)
    hbar.config(command=canvas.xview)
    vbar = Scrollbar(frame, orient=VERTICAL)
    vbar.pack(side=RIGHT, fill=Y)
    vbar.config(command=canvas.yview)
    canvas.config(width=800, height=600)
    canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
    canvas.pack(side=LEFT, expand=True, fill=BOTH)

    for position, state in enumerate(turing_machine.states):
        state_position[state] = position
        loop_occurrences[position] = 0
        canvas_id = canvas.create_text(10 + 80 * position, 400, anchor="nw")
        canvas.itemconfig(canvas_id, text="state-")
        canvas.insert(canvas_id, 12, "%d" % state)

    counter = 1
    for rule in turing_machine.rules:
        counter = draw_arrow(state_position[rule.current_state],
                             state_position[rule.next_state],
                             canvas, counter, rule)

    root.mainloop()
