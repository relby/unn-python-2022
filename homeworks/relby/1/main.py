#!/usr/bin/env python
from typing import Tuple, List
from sys import stderr
from os import path
import csv

QUESTIONS_FILEPATH = './questions.csv'

QuestionType = Tuple[str, str]


def load_questions_from_csv(filepath: str) -> List[QuestionType]:
    with open(filepath, 'r') as file:
        reader = csv.reader(file)
        try:
            return [(question.strip(), answer.strip()) for question, answer in reader]
        except ValueError:
            print("Ошибка в csv файле. Каждая строка должна содержать "
                  "данные в таком формате: <question>,<answer>", file=stderr)
            exit(1)


def main():
    filepath = path.join(path.dirname(__file__), QUESTIONS_FILEPATH)
    questions = load_questions_from_csv(filepath)

    right_answers = 0
    for question, answer in questions:
        user_answer = input(f"{question}: ")
        if user_answer.lower() == answer.lower():
            print(f"Ответ {user_answer} верен.")
            right_answers += 1
        else:
            print(f"Неверный ответ. Правильный ответ - {answer}.")

    print("Вы дали {} правильных ответов и {} неправильных."
          .format(right_answers, len(questions) - right_answers))


if __name__ == "__main__":
    main()
