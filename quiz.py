class Quiz:
    def __init__(self, question, choices, answer):
        if not isinstance(question, str) or not question.strip():
            raise ValueError("문제는 빈 문자열이 아닌 글자여야 합니다.")

        if not isinstance(choices, list) or len(choices) != 4:
            raise ValueError("선택지는 4개를 담은 목록이어야 합니다.")

        for choice in choices:
            if not isinstance(choice, str) or not choice.strip():
                raise ValueError("선택지는 빈 문자열이 아닌 글자여야 합니다.")

        if type(answer) is not int or not 1 <= answer <= 4:
            raise ValueError("정답 번호는 1~4 사이의 정수여야 합니다.")

        self.question = question.strip()
        self.choices = [choice.strip() for choice in choices]
        self.answer = answer

    def display(self):
        print(self.question)

        for number, choice in enumerate(self.choices, start=1):
            print(f"{number}. {choice}")

    def check_answer(self, user_answer):
        return user_answer == self.answer

    def to_dict(self):
        return {
            "question": self.question,
            "choices": self.choices.copy(),
            "answer": self.answer,
        }

    @classmethod
    def from_dict(cls, data):
        if not isinstance(data, dict):
            raise ValueError("퀴즈 데이터는 딕셔너리여야 합니다.")

        required_keys = ("question", "choices", "answer")
        for key in required_keys:
            if key not in data:
                raise ValueError(f"퀴즈 데이터에 {key} 항목이 없습니다.")

        return cls(data["question"], data["choices"], data["answer"])


if __name__ == "__main__":
    sample_quiz = Quiz(
        question="1 + 1의 값은?",
        choices=["1", "2", "3", "4"],
        answer=2,
    )

    sample_quiz.display()
    print("2번 선택 결과:", sample_quiz.check_answer(2))
    print("1번 선택 결과:", sample_quiz.check_answer(1))

    data = sample_quiz.to_dict()
    print("딕셔너리 변환:", data)

    restored_quiz = Quiz.from_dict(data)
    print("복원한 문제:", restored_quiz.question)
    print("복원 후 정답 확인:", restored_quiz.check_answer(2))

    try:
        Quiz("잘못된 정답 번호 검사", ["가", "나", "다", "라"], 0)
    except ValueError as error:
        print("잘못된 데이터 차단:", error)