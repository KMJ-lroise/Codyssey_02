from quiz import Quiz


def create_default_quizzes():
    return [
        Quiz(
            question="아이언맨이 사용하는 AI 비서의 이름은?",
            choices=["자비스", "빅스비", "알렉사", "시리"],
            answer=1,
        ),
        Quiz(
            question="코디세이 과정에서 사용하는 AI 이름은?",
            choices=["네이버", "제미나이", "네이토", "클로드"],
            answer=3,
        ),
        Quiz(
            question="AI는 무엇의 약자일까요?",
            choices=["Automated Integration", "Artificial Intelligence", "Advanced Interface", "Autonomous Infrastructure"],
            answer=2,
        ),
        Quiz(
            question="AI를 활용해서 소프트웨어를 개발하는 방법을 뭐라고 부를까요?",
            choices=["머신 러닝", "파이썬코딩", "딥코딩", "바이브코딩"],
            answer=4,
        ),
        Quiz(
            question="프로그래밍에 사용되는 언어가 아닌 것은?",
            choices=["Python", "Java", "git", "C++"],
            answer=3,
        ),
    ]


if __name__ == "__main__":
    quizzes = create_default_quizzes()

    print(f"기본 퀴즈 개수: {len(quizzes)}")

    for number, quiz in enumerate(quizzes, start=1):
        print()
        print(f"[문제 {number}]")
        quiz.display()
        print(f"정답 번호: {quiz.answer}")

- default_quizzes.py: 기본 퀴즈를 Quiz 객체로 생성하고 목록으로 반환합니다.