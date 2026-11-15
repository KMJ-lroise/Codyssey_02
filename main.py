import json
from pathlib import Path
from default_quizzes import create_default_quizzes


LANGUAGE_FILE = Path(__file__).with_name("language.json")
DEFAULT_LANGUAGE = "ko"
LANGUAGES = {
    "ko": {
        "empty_input": "입력이 비어 있습니다. 숫자를 입력하세요.",
        "invalid_number": "숫자로 바꿀 수 없습니다. 정수를 입력하세요.",
        "out_of_range": "{min_value}~{max_value} 사이의 숫자를 입력하세요.",
        "title": "나만의 퀴즈 게임",
        "solve_quiz": "퀴즈 풀기",
        "add_quiz": "퀴즈 추가",
        "quiz_list": "퀴즈 목록",
        "check_score": "점수 확인",
        "configure_language": "표시 언어 설정",
        "exit": "종료",
        "select_prompt": "선택: ",
        "solve_selected": "퀴즈 풀기를 선택했습니다. 구현 예정입니다.",
        "add_selected": "퀴즈 추가를 선택했습니다. 구현 예정입니다.",
        "list_selected": "퀴즈 목록을 선택했습니다. 구현 예정입니다.",
        "score_selected": "점수 확인을 선택했습니다. 구현 예정입니다.",
        "language_prompt": "표시 언어를 선택하세요:",
        "korean": "한국어",
        "english": "영어",
        "language_saved": "표시 언어를 한국어로 설정했습니다.",
        "language_save_failed": "언어 설정을 저장하지 못했습니다: {error}",
        "exit_message": "퀴즈 게임을 종료합니다.",
        "interrupt": "\nCtrl+C를 감지했습니다. 프로그램을 종료합니다.",
        "eof": "\n입력이 종료되었습니다. 프로그램을 종료합니다.",
        "no_quizzes": "등록된 퀴즈가 없습니다.",
        "quiz_start": "퀴즈를 시작합니다! (총 {total}문제)",
        "question_number": "[문제 {number}]",
        "answer_prompt": "정답 번호 (1~4): ",
        "correct_answer": "정답입니다!",
        "wrong_answer": "오답입니다. 정답은 {answer}번입니다.",
        "quiz_result": "결과: {total}문제 중 {correct}문제 정답! ({score}점)",
    },
    "en": {
        "empty_input": "Input is empty. Please enter a number.",
        "invalid_number": "That is not a valid integer. Please enter an integer.",
        "out_of_range": "Please enter a number between {min_value} and {max_value}.",
        "title": "My Quiz Game",
        "solve_quiz": "Play a quiz",
        "add_quiz": "Add a quiz",
        "quiz_list": "Quiz list",
        "check_score": "Check score",
        "configure_language": "Configure display language",
        "exit": "Exit",
        "select_prompt": "Select: ",
        "solve_selected": "You selected Play a quiz. Coming soon.",
        "add_selected": "You selected Add a quiz. Coming soon.",
        "list_selected": "You selected Quiz list. Coming soon.",
        "score_selected": "You selected Check score. Coming soon.",
        "language_prompt": "Choose a display language:",
        "korean": "Korean",
        "english": "English",
        "language_saved": "Display language set to English.",
        "language_save_failed": "Could not save the language setting: {error}",
        "exit_message": "Exiting the quiz game.",
        "interrupt": "\nCtrl+C detected. Exiting the program.",
        "eof": "\nInput ended. Exiting the program.",
        "no_quizzes": "There are no quizzes.",
        "quiz_start": "Starting the quiz! ({total} questions)",
        "question_number": "[Question {number}]",
        "answer_prompt": "Answer (1-4): ",
        "correct_answer": "Correct!",
        "wrong_answer": "Incorrect. The correct answer is {answer}.",
        "quiz_result": "Result: {correct}/{total} correct! ({score} points)",
    },
}


def message(key, language, **values):
    return LANGUAGES[language][key].format(**values)


def load_language():
    try:
        with LANGUAGE_FILE.open(encoding="utf-8") as settings_file:
            settings = json.load(settings_file)

        if not isinstance(settings, dict):
            raise ValueError("언어 설정은 딕셔너리 형태여야 합니다.")

        language = settings.get("language")

        if not isinstance(language, str) or language not in LANGUAGES:
            raise ValueError("지원하지 않는 언어 설정입니다.")

        return language

    except FileNotFoundError:
        return DEFAULT_LANGUAGE

    except (OSError, ValueError) as error:
        print(f"언어 설정을 읽을 수 없어 한국어로 시작합니다: {error}")
        print("Could not load language settings. Starting in Korean.")
        return DEFAULT_LANGUAGE


def save_language(language):
    if language not in LANGUAGES:
        raise ValueError(f"Unsupported language: {language!r}")

    with LANGUAGE_FILE.open("w", encoding="utf-8") as settings_file:
        json.dump({"language": language}, settings_file, ensure_ascii=False, indent=2)
        settings_file.write("\n")


def read_int(prompt, min_value, max_value, language=DEFAULT_LANGUAGE):
    while True:
        text = input(prompt).strip()

        if text == "":
            print(message("empty_input", language))
            continue

        try:
            number = int(text)
        except ValueError:
            print(message("invalid_number", language))
            continue

        if not min_value <= number <= max_value:
            print(message("out_of_range", language, min_value=min_value, max_value=max_value))
            continue

        return number


def show_menu(language=DEFAULT_LANGUAGE):
    labels = LANGUAGES[language]
    print()
    print("=" * 40)
    print(labels["title"])
    print("=" * 40)
    print(f"1. {labels['solve_quiz']}")
    print(f"2. {labels['add_quiz']}")
    print(f"3. {labels['quiz_list']}")
    print(f"4. {labels['check_score']}")
    print(f"5. {labels['configure_language']}")
    print(f"6. {labels['exit']}")
    print("=" * 40)


def configure_language(current_language):
    print(message("language_prompt", current_language))
    print(f"1. {message('korean', current_language)}")
    print(f"2. {message('english', current_language)}")
    selection = read_int(message("select_prompt", current_language), 1, 2, current_language)
    selected_language = "ko" if selection == 1 else "en"

    try:
        save_language(selected_language)
    except OSError as error:
        print(message("language_save_failed", current_language, error=error))
        return current_language

    print(message("language_saved", selected_language))
    return selected_language


def play_quiz(quizzes, language=DEFAULT_LANGUAGE):
    if not quizzes:
        print(message("no_quizzes", language))
        return

    total = len(quizzes)
    correct_count = 0
    print(message("quiz_start", language, total=total))

    for number, quiz in enumerate(quizzes, start=1):
        print()
        print("-" * 40)
        print(message("question_number", language, number=number))
        quiz.display()

        user_answer = read_int(
            message("answer_prompt", language),
            1,
            4,
            language,
        )

        if quiz.check_answer(user_answer):
            correct_count += 1
            print(message("correct_answer", language))
        else:
            print(message("wrong_answer", language, answer=quiz.answer))

    score = round(correct_count / total * 100)
    print()
    print(
        message(
            "quiz_result",
            language,
            total=total,
            correct=correct_count,
            score=score,
        )
    )
    return score


class QuizGame:
    def __init__(self):
        self.quizzes = create_default_quizzes()
        self.best_score = None
        self.language = load_language()

    def show_menu(self):
        show_menu(self.language)

    def play_quiz(self):
        return play_quiz(self.quizzes, self.language)

    def configure_language(self):
        self.language = configure_language(self.language)

    def run(self):
        try:
            while True:
                self.show_menu()
                choice = read_int(
                    message("select_prompt", self.language),
                    1,
                    6,
                    self.language,
                )

                if choice == 1:
                    self.play_quiz()
                elif choice == 2:
                    print(message("add_selected", self.language))
                elif choice == 3:
                    print(message("list_selected", self.language))
                elif choice == 4:
                    print(message("score_selected", self.language))
                elif choice == 5:
                    self.configure_language()
                elif choice == 6:
                    print(message("exit_message", self.language))
                    break

        except KeyboardInterrupt:
            print(message("interrupt", self.language))
        except EOFError:
            print(message("eof", self.language))


def run_game():
    game = QuizGame()
    game.run()


if __name__ == "__main__":
    try:
        run_game()
    except (OSError, ValueError) as error:
        print(f"언어 설정을 불러오지 못했습니다 / Could not load the language setting: {error}")
        raise SystemExit(1)
