import random
import tkinter as tk


class SubtractionGame:
    def __init__(self, master):
        self.master = master
        master.title("Subtraction Game")

        self.score = 0

        # Create label for problem
        self.problem_label = tk.Label(master, text="")
        self.problem_label.pack()

        # Create entry for answer
        self.answer_entry = tk.Entry(master)
        self.answer_entry.pack()

        # Create button to check answer
        self.check_button = tk.Button(master, text="Check Answer", command=self.check_answer)
        self.check_button.pack()

        # Create label for message
        self.message_label = tk.Label(master, text="")
        self.message_label.pack()

        # Create label for score
        self.score_label = tk.Label(master, text=f"Score: {self.score}")
        self.score_label.pack()

        # Create button for next problem
        self.next_button = tk.Button(master, text="Next Problem", command=self.next_problem)
        self.next_button.pack()

        # Create exit button
        self.exit_button = tk.Button(master, text="Exit", command=master.quit)
        self.exit_button.pack()

        # Generate first problem
        self.generate_problem()

    def generate_problem(self):
        self.num1 = random.randint(1, 100)
        self.num2 = random.randint(1, 100)
        self.problem_label.config(text=f"{self.num1} - {self.num2} = ")
        self.answer_entry.delete(0, tk.END)
        self.message_label.config(text="")

    def check_answer(self):
        try:
            user_answer = int(self.answer_entry.get())
            correct_answer = self.num1 - self.num2
            if user_answer == correct_answer:
                self.score += 1
                self.message_label.config(text=random.choice(["Great job!", "You're a math whiz!", "Keep it up!"]))
            else:
                self.message_label.config(text=f"Sorry, the correct answer is {correct_answer}")
        except ValueError:
            self.message_label.config(text="Please enter a number")

        self.score_label.config(text=f"Score: {self.score}")

    def next_problem(self):
        self.generate_problem()


root = tk.Tk()
game = SubtractionGame(root)
root.mainloop()