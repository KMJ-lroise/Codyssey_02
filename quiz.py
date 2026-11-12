class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def display(self):
        print(self.question)

        for number, choice in enumerate(self.choices, start=1):
            print(f"{number}. {choice}")

    def check_answer(self, user_answer):
        return user_answer == self.answer


if __name__ == "__main__":
    sample_quiz = Quiz(
        question="1 + 1의 값은?",
        choices=["1", "2", "3", "4"],
        answer=2,
    )

    sample_quiz.display()
    print("2번 선택 결과:", sample_quiz.check_answer(2))
    print("1번 선택 결과:", sample_quiz.check_answer(1))
    