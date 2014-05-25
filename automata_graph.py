from tkinter import *
master = Tk()
w = Canvas(master, width=800, height=800)



def quadratic(x,a):
    return (8*a*a*a)/(x*x+4*a*a)


def draw_arrow(i, j):
    x1 = (10+80*i) + 15
    x2 = (10+80*j)
    diff = (x2 + x1 + 15) / 2
    if i == j:
        # w.create_oval(x2, 390, x1 , 410)
        w.create_oval(x2, 390-10, x1+5+5 , 410)
        w.create_line(x1-5+7, 400, x1+7, 405, width=2,fill="black")
        w.create_line(x1+5+7, 400, x1+7, 405, width=2,fill="black")
    elif i+1 == j:
        w.create_line(x1, 405, x2, 405, width=2,fill="green")
        w.create_line(x2-5, 400, x2, 405, width=2,fill="green")
        w.create_line(x2-5, 410, x2, 405, width=2,fill="green")
        return
    elif j+1 == i:
        w.create_line(x1, 405, x2, 405, width=2,fill="green")    
        w.create_line(x1, 405, x2-5, 400, width=2,fill="green")    
        w.create_line(x1, 405, x2-5, 410, width=2,fill="green")    
    while x1 <= x2+15:
        w.create_line(x1, quadratic(x1-diff,(abs(i-j))*5+10)+400, x1+3, quadratic(x1+3-diff,(abs(i-j))*5+10)+400, width=2,fill="blue")
        x1 += 3


def draw_automata(turing_machine):

    master.protocol("WM_DELETE_WINDOW", master.quit())
    Button(master, text='Quit', command=master.quit).pack(side=BOTTOM, anchor=SE)
    w.pack()


    for i in range(len(turing_machine.states)): 
        canvas_id = w.create_text(10 + 80 * i, 400, anchor="nw")
        w.itemconfig(canvas_id, text="state-")
        w.insert(canvas_id, 12 , "%d" % i)

    for rule in turing_machine.rules:
        draw_arrow(rule.current_state, rule.next_state)

    master.mainloop()
