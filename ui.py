from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("QUIZ")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.tick = PhotoImage(file="images/true.png")
        self.false = PhotoImage(file="images/false.png")

        self.score_label = Label(text=f"Score=", bg=THEME_COLOR, font=("Arial", 15))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=250,
            text="Some text.",
            fill=THEME_COLOR,
            font=("Arial", 15)
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady= 35)

        self.tick_button = Button(image=self.tick, highlightthickness=0, bg=THEME_COLOR, command=self.true_pressed)
        self.tick_button.grid(row=2, column=0, pady=4, padx=3)

        self.false_button = Button(image=self.false, highlightthickness=0, bg=THEME_COLOR, command= self.false_pressed)
        self.false_button.grid(row=2, column=1, pady=4, padx=3)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score:{self.quiz.score}")
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
