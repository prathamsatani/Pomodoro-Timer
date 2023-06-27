from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
tick = '✔'

# ------------------------ TICK MARK MECHANISM --------------------------- #


def insert_tick():
    insert_tick.add_str += tick
    label2.config(text=insert_tick.add_str)


def reset_tick():
    insert_tick.add_str = ""
    label2.config(text=insert_tick.add_str)


insert_tick.add_str = ""


# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    reps = 0
    reset_tick()
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label1.config(text='Timer')

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 20

    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(long_break_sec)
        label1.config(fg=RED, text='BREAK')
    elif reps % 2 == 0:
        insert_tick()
        count_down(short_break_sec)
        label1.config(fg=PINK, text='BREAK')
    else:
        count_down(work_sec)
        label1.config(fg=GREEN, text='WORK')


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    count_min = int(count / 60)
    count_sec = count % 60
    global timer
    if len(str(count_sec)) < 2:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title(string='Pomodoro App')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas()
canvas.config(width=200, height=224, bg=YELLOW, highlightthickness=0)
image_add = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=image_add)
timer_text = canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)

label1 = Label()
label1.config(text='Timer', font=(FONT_NAME, 35, 'bold'), fg=GREEN, bg=YELLOW)
label1.grid(row=0, column=1)

label2 = Label()
label2.config(text='', fg=GREEN, bg=YELLOW)
label2.grid(row=3, column=1)

button1 = Button(text='Start', highlightthickness=0, command=start_timer)
button1.grid(row=2, column=0)

button1 = Button(text='Reset', highlightthickness=0, command=reset_timer)
button1.grid(row=2, column=2)
window.mainloop()
