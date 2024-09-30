import tkinter
import math

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
next_session = None  # Variable to track the next session


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timer
    if timer is not None:
        window.after_cancel(timer)  # Cancel the ongoing timer if there's one running
    canvas.itemconfig(timer_text, text="00:00")  # Reset the timer display
    title_label.config(text="Timer")  # Reset the title label
    check_marks.config(text="")  # Clear the checkmarks
    global reps
    reps = 0  # Reset the repetition count
    start_button.config(state="normal")  # Re-enable the Start button
    timer = None  # Reset the timer value to None


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    global next_session
    reps += 1  # Increment repetition count
    start_button.config(
        state="disabled"
    )  # Disable the Start button while the session is running

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if next_session == "long_break":
        count_down(long_break_sec)  # Long break after 4 work sessions
        title_label.config(text="Long Break", fg=RED)
    elif next_session == "short_break":
        count_down(short_break_sec)  # Short break after each work session
        title_label.config(text="Short Break", fg=PINK)
    else:
        count_down(work_sec)  # Work session
        title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"  # Display single digits as two digits

    canvas.itemconfig(
        timer_text, text=f"{count_min}:{count_sec}"
    )  # Update the timer display

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)  # Call countdown every second
    else:
        session_complete()  # Call session_complete() after the session ends


# ---------------------------- SESSION COMPLETE ------------------------------- #
def session_complete():
    global reps, next_session
    marks = ""
    work_sessions = math.floor(reps / 2)
    for _ in range(work_sessions):
        marks += "✔"  # Add a checkmark for each completed work session
    check_marks.config(text=marks)

    # Update the session type for the next session
    if reps % 8 == 0:  # If 8 reps, next will be work after long break
        next_session = "work"
        title_label.config(text="Work", fg=GREEN)
    elif reps % 2 == 0:  # If even, next will be work after short break
        next_session = "work"
        title_label.config(text="Work", fg=GREEN)
    else:  # If odd, next will be a short break
        if reps % 8 == 7:  # After the 7th rep, the next is a long break
            next_session = "long_break"
            title_label.config(text="Long Break", fg=RED)
        else:
            next_session = "short_break"
            title_label.config(text="Short Break", fg=PINK)

    start_button.config(
        state="normal"
    )  # Re-enable the Start button after the session ends


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=150, pady=75, bg=YELLOW)  # Increased window size

# Title label
title_label = tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40))
title_label.grid(column=1, row=0)

# Canvas for timer and image
canvas = tkinter.Canvas(
    width=400, height=300, bg=YELLOW, highlightthickness=0
)  # Increased canvas size
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(200, 150, image=tomato_img)  # Adjusted image position
timer_text = canvas.create_text(
    200, 170, text="00:00", fill="white", font=(FONT_NAME, 25, "bold")
)
canvas.grid(column=1, row=1)

# Start and reset buttons
start_button = tkinter.Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = tkinter.Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# Label for checkmarks
check_marks = tkinter.Label(
    fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20)
)  # Adjusted font for checkmarks
check_marks.grid(column=1, row=3)

window.mainloop()
