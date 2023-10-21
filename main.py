from tkinter import *
import random
from tkinter.messagebox import showerror

numbers = []
current_number = 0
quantity = 2


def start_game():
    global numbers, current_number
    numbers = [random.randint(1, 100) for _ in range(quantity)]
    entry.delete(0, END)
    entry.config(state=DISABLED)
    evaluate_button.config(state=DISABLED)
    result_label.config(text="")
    current_number = 0
    show_number()


def show_number():
    start_button.config(state=DISABLED)
    number_label.config(text=numbers[current_number])
    number_label.after(1000, hide_number)


def hide_number():
    global current_number
    number_label.config(text="")
    current_number += 1
    if current_number < len(numbers):
        number_label.after(2000, show_number)
    else:
        start_button.config(state=NORMAL)
        entry.config(state=NORMAL)
        evaluate_button.config(state=NORMAL)


def evaluate_game():
    user_input = entry.get()
    user_numbers = list(map(str, user_input.split()))
    if len(user_numbers) > quantity:
        showerror(title="Error", message="Numbers overflow!")
    else:
        if all(i.isdigit() for i in user_numbers) and user_numbers:
            correct_numbers = numbers[:len(user_numbers)]
            score = sum([int(user_numbers[i]) == correct_numbers[i] for i in range(len(user_numbers))])
            result_label.config(text=f"Вы правильно запомнили {score}/{quantity} чисел")
        else:
            showerror(title="Error", message="int, not str!")


root = Tk()
root.title("Оценка способности запоминать числа")
root.geometry('400x400')

start_button = Button(root, text="Старт", command=start_game)
start_button.pack()

number_label = Label(root, text="")
number_label.pack()

entry = Entry(root, state=DISABLED)
entry.pack()

evaluate_button = Button(root, text="Оценить", command=evaluate_game, state=DISABLED)
evaluate_button.pack()

result_label = Label(root, text="")
result_label.pack()

root.mainloop()
