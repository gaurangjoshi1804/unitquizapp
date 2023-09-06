import tkinter as tk
import tkinter.font as tkfont
from tkinter import messagebox
from string import ascii_lowercase

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Unit Quiz App")
        self.root.geometry("400x300")
        self.root['bg']="Sky Blue"
        self.title_font = tkfont.Font(family="Helvetica", size=16, weight="bold", underline=True)

        self.questions = {
            "1). Brass gets discoloured in air because of the presence of which of the following gases in air?": [
                "Oxygen",
                "Hydrogen sulphide",
                "Carbon dioxide",
                "Nitrogen"],
            "2). Which of the following is a non metal that remains liquid at room temperature?": [
                "Phosphorous",
                "Bromine",
                "Chlorine",
                "Helium"],
            "3).Chlorophyll is a naturally occurring chelate compound in which central metal is": [
                "copper",
                "magnesium",
                "iron",
                "calcium"],
            "4). Which of the following is used in pencils?":[
                "Graphite",
                "Silicon",
                "Charcoal",
                "Phosphorous"],
            "5). Which of the following metals forms an amalgam with other metals?":[
                "Tin",
                "Mercury",
                "Lead",
                "Zinc"],
            }
        
        self.num_correct = 0
        self.current_question = 0

        self.init_widgets()
    def init_widgets(self):
        self.title_label = tk.Label(self.root, text="Test Your Knowledge", font=self.title_font)
        self.title_label.pack()

        self.start_button = tk.Button(self.root, text="Start", command=self.start_quiz)
        self.start_button.pack()
        
    def start_quiz(self):
        self.start_button.destroy()
        self.ask_question()

    def ask_question(self):
        if self.current_question < len(self.questions):
            question, alternatives = list(self.questions.items())[self.current_question]
            self.question_label = tk.Label(self.root, text=f"Question {self.current_question + 1}:", font=self.title_font)
            self.question_label.pack()

            self.question_text = tk.Label(self.root, text=question)
            self.question_text.pack()

            self.correct_answer = alternatives[0]
            self.labeled_alternatives = dict(zip(ascii_lowercase, sorted(alternatives)))
            for label, alternative in self.labeled_alternatives.items():
                alternative_text = f"  {label}) {alternative}"
                alternative_label = tk.Label(self.root, text=alternative_text)
                alternative_label.pack()

            self.answer_label = tk.Label(self.root, text="Choice?")
            self.answer_label.pack()

            self.answer_entry = tk.Entry(self.root)
            self.answer_entry.pack()

            self.check_button = tk.Button(self.root, text="Check Answer", command=self.check_answer)
            self.check_button.pack()

            self.result_label = tk.Label(self.root, text="")
            self.result_label.pack()
        else:
            self.show_score()

    def check_answer(self):
        user_answer = self.answer_entry.get()
        answer = self.labeled_alternatives.get(user_answer)
        if answer == self.correct_answer:
            self.num_correct += 1
            self.result_label.config(text="Correct!", fg="green")
        else:
            self.result_label.config(text=f"The answer is {self.correct_answer!r}, not {answer!r}", fg="red")
        self.check_button.config(state="disabled")
        self.current_question += 1
        self.clear_question()

    def clear_question(self):
        self.question_label.destroy()
        self.question_text.destroy()
        self.answer_label.destroy()
        self.answer_entry.destroy()
        self.check_button.destroy()
        self.result_label.destroy()
        self.ask_question()

    def show_score(self):
        score_label = tk.Label(self.root, text=f"You got {self.num_correct} correct out of {len(self.questions)} questions")
        score_label.pack()

        end_label = tk.Label(self.root, text="This is the end of the quiz. You've done a great job!", font=self.title_font)
        end_label.pack()
        
        replay_button = tk.Button(self.root, text="Replay Quiz", command=self.replay_quiz)
        replay_button.pack()
        
        for widget in self.root.winfo_children():
            widget.destroy()
        
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()






        
            





    
    
    

    
