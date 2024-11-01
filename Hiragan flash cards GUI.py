import json
import requests
import random
from tkinter import *
from tkinter import messagebox

url = "https://raw.githubusercontent.com/Katherine-Brown-8000/Hiragana_flash_cards/refs/heads/main/Hiragana.json"
response = requests.get(url)

if response.status_code == 200:
    hiragana = json.loads(response.text)
else:
    print("Failed to retrieve the data")
    hiragana = {}

class HiraganaFlashCards(Frame):
    def __init__(self, root):
        self.root = root
        self.root.title("Hiragana Flash Cards")

        self.q_count = 0
        self.score = 0
        self.current_question = 0
        self.selected_char = ""
        self.correct_answer = []

        self.prompt_label = Label(self.root, text="Enter the number of flash cards you would like to do: ")
        self.prompt_label.grid(row=0, column=0)

        self.q_count_entry = Entry(self.root, width=10)
        self.q_count_entry.grid(row=2, column=0)

        self.start_button = Button(self.root, text="start Quiz", command=self.start_quiz)
        self.start_button.grid(row=0, column=2)

        self.canvas = Canvas(self.root, width=500, height=300, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=3)

        self.label = Label(self.root, text="Type your answer: ")
        self.label.grid(row=2, column=0)

        self.entry = Entry(self.root, width=300)
        self.entry.grid(row=2, column=1)

        self.submit_button = Button(self.root, text="Submit", command=self.check_answer)
        self.submit_button.grid(row=3, column=0, columnspan=3)

        self.hide_quiz_elements()

    def hide_quiz_elements(self):
        self.canvas.grid_remove()
        self.label.grid_remove()
        self.entry.grid_remove()
        self.submit_button.grid_remove()

    def show_quiz_elements(self):
         self.canvas.grid()
         self.label.grid()
         self.entry.grid()
         self.submit_button.grid()

    def start_quiz(self):
         try:
             self.q_count = int(self.q_count_entry.get())
             if self.q_count <= 0:
                 raise ValueError("Please enter a positive number.")
         except ValueError:
             messagebox.showerror("Invalid Input", "Please enter a valid number of questions")
             return

         self.prompt_label.grid_remove()
         self.q_count_entry.grid_remove()
         self.start_button.grid_remove()
         self.show_quiz_elements()

         self.next_question()

    def next_question(self):
         if self.current_question < self.q_count:
             self.selected_char, self.correct_answer = random.choice(list(hiragana.items()))
             self.canvas.delete("all")
             self.canvas.create_text(250, 150, text=self.selected_char, font=("Arial", 60))
             self.entry.delete(0, END)
             self.current_question += 1
         else:
             self.show_score()

    def check_answer(self):
        answer = self.entry.get().strip().lower()

        if isinstance(self.correct_answer, list):
            correct_answers_lower = [ans.lower() for ans in self.correct_answer]
            if answer in correct_answers_lower:
                self.score += 1
        elif isinstance(self.correct_answer, str) and answer == self.correct_answer.lower():
            self.score += 1

        self.next_question()

    def show_score(self):
        total_score = (self.score / self.q_count) * 100
        messagebox.showinfo("Quiz completed", f"Your score is: {total_score}")

root = Tk()
app = HiraganaFlashCards(root)
root.mainloop()
