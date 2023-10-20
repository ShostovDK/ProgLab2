from tkinter import *
import random

numbers = []
current_number = 0
quantity = 2


def start_game():
    global numbers, current_number, quantity
    numbers = [random.randint(1, 100) for _ in range(quantity)]
    current_number = 0
    show_number()


def show_number():
    number_label.config(text=numbers[current_number])
    number_label.after(1000, hide_number)


def hide_number():
    global current_number
    number_label.config(text="")
    current_number += 1
    if current_number < len(numbers):
        number_label.after(2000, show_number)
    else:
        evaluate_game()


def evaluate_game():
    user_input = entry.get()
    user_numbers = list(map(int, user_input.split()))
    correct_numbers = numbers[:len(user_numbers)]
    score = sum([user_numbers[i] == correct_numbers[i] for i in range(len(user_numbers))])
    result_label.config(text=f"Вы правильно запомнили {score}/{quantity} чисел")


root = Tk()
root.title("Оценка способности запоминать числа")

start_button = Button(root, text="Старт", command=start_game)
start_button.pack()

number_label = Label(root, text="")
number_label.pack()

entry = Entry(root)
entry.pack()

evaluate_button = Button(root, text="Оценить", command=evaluate_game)
evaluate_button.pack()

result_label = Label(root, text="")
result_label.pack()

root.mainloop()
