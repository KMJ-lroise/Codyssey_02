import json
from pathlib import Path
from default_quizzes import create_default_quizzes
from quiz import Quiz
from datetime import datetime


LANGUAGE_FILE = Path(__file__).with_name("language.json")
STATE_FILE = Path(__file__).resolve().with_name("state.json")
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
        "empty_text": "내용이 비어 있습니다. 다시 입력하세요.",
        "add_start": "새로운 퀴즈를 추가합니다.",
        "question_prompt": "문제를 입력하세요: ",
        "choice_prompt": "선택지 {number}: ",
        "quiz_added": "퀴즈가 추가되었습니다! (총 {total}개)",
        "quiz_list_title": "등록된 퀴즈 목록 (총 {total}개)",
        "no_score": "아직 퀴즈를 끝까지 풀지 않았습니다.",
        "best_score_display": "최고 점수: {score}점",
        "new_best_score": "새로운 최고 점수입니다! ({score}점)",
        "state_missing": "저장 파일이 없어 기본 퀴즈로 시작합니다.",
        "state_loaded": "저장된 데이터를 불러왔습니다. (퀴즈 {total}개)",
        "state_invalid": "저장 데이터가 손상되어 기본 퀴즈로 시작합니다: {error}",
        "state_backup": "손상 파일을 백업했습니다: {filename}",
        "state_backup_failed": "백업하지 못해 이번 실행의 저장을 중지합니다: {error}",
        "state_read_failed": "파일을 읽지 못했습니다. 기본 퀴즈로 시작하며 이번 실행은 저장하지 않습니다: {error}",
        "state_save_blocked": "기존 파일 보호를 위해 저장하지 않았습니다.",
        "state_save_failed": "파일 저장에 실패했습니다. 이번 변경이 저장되지 않았습니다: {error}",
        "state_save_interrupted": "파일 저장이 중단되었습니다. 저장 완료를 확인하지 못했습니다.",
        "state_saved": "퀴즈와 최고 점수를 저장했습니다.",
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
        "empty_text": "Input is empty. Please enter some text.",
        "add_start": "Add a new quiz.",
        "question_prompt": "Enter a question: ",
        "choice_prompt": "Choice {number}: ",
        "quiz_added": "Quiz added! ({total} quizzes in total)",
        "quiz_list_title": "Quiz list ({total} quizzes)",
        "no_score": "You have not completed a quiz yet.",
        "best_score_display": "Best score: {score} points",
        "new_best_score": "New best score! ({score} points)",
        "state_missing": "No save file. Starting with default quizzes.",
        "state_loaded": "Saved data loaded. ({total} quizzes)",
        "state_invalid": "Invalid save data. Starting with default quizzes: {error}",
        "state_backup": "Damaged file backed up: {filename}",
        "state_backup_failed": "Backup failed. Saving is disabled for this session: {error}",
        "state_read_failed": "Could not read the file. Using defaults without saving this session: {error}",
        "state_save_blocked": "Saving skipped to protect the existing file.",
        "state_save_failed": "Save failed. These changes were not saved: {error}",
        "state_save_interrupted": "Saving was interrupted. Save completion could not be confirmed.",
        "state_saved": "Quizzes and best score saved.",
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


def read_text(prompt, language=DEFAULT_LANGUAGE):
    while True:
        text = input(prompt).strip()

        if text:
            return text

        print(message("empty_text", language))


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
        self.can_save = True
        self.load_state()

    def load_state(self):
        try:
            with STATE_FILE.open(encoding="utf-8") as state_file:
                data = json.load(state_file)

            if not isinstance(data, dict):
                raise ValueError("state data must be an object.")
            if "quizzes" not in data or "best_score" not in data:
                raise ValueError("quizzes or best_score is missing.")
            if not isinstance(data["quizzes"], list):
                raise ValueError("quizzes must be a list.")

            quizzes = [Quiz.from_dict(item) for item in data["quizzes"]]
            best_score = data["best_score"]

            if best_score is not None:
                if type(best_score) is not int or not 0 <= best_score <= 100:
                    raise ValueError(
                        "best_score must be null or an integer from 0 to 100."
                    )

        except FileNotFoundError:
            print(message("state_missing", self.language))

        except (ValueError, RecursionError) as error:
            print(message("state_invalid", self.language, error=error))

            stamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
            backup = STATE_FILE.with_name(
                STATE_FILE.name + f".corrupt-{stamp}.bak"
            )

            try:
                STATE_FILE.rename(backup)
            except OSError as backup_error:
                self.can_save = False
                print(
                    message(
                        "state_backup_failed",
                        self.language,
                        error=backup_error,
                    )
                )
            else:
                print(
                    message(
                        "state_backup",
                        self.language,
                        filename=backup.name,
                    )
                )

        except OSError as error:
            self.can_save = False
            print(message("state_read_failed", self.language, error=error))

        else:
            self.quizzes = quizzes
            self.best_score = best_score
            print(
                message(
                    "state_loaded",
                    self.language,
                    total=len(self.quizzes),
                )
            )

    def save_state(self):
        if not self.can_save:
            print(message("state_save_blocked", self.language))
            return False

        temp_file = STATE_FILE.with_name(STATE_FILE.name + ".tmp")

        try:
            data = {
                "quizzes": [quiz.to_dict() for quiz in self.quizzes],
                "best_score": self.best_score,
            }

            with temp_file.open("w", encoding="utf-8") as state_file:
                json.dump(data, state_file, ensure_ascii=False, indent=2)
                state_file.write("\n")

            temp_file.replace(STATE_FILE)

        except (OSError, ValueError, TypeError) as error:
            print(message("state_save_failed", self.language, error=error))
            return False

        except KeyboardInterrupt:
            print(message("state_save_interrupted", self.language))
            return False

        print(message("state_saved", self.language))
        return True

    def show_menu(self):
        show_menu(self.language)

    def play_quiz(self):
        score = play_quiz(self.quizzes, self.language)

        if score is None:
            return

        if self.best_score is None or score > self.best_score:
            self.best_score = score
            print(message("new_best_score", self.language, score=score))

        self.save_state()
        return score

    def show_score(self):
        if self.best_score is None:
            print(message("no_score", self.language))
            return

        print(
            message(
                "best_score_display",
                self.language,
                score=self.best_score,
            )
        )

    def add_quiz(self):
        print(message("add_start", self.language))

        question = read_text(
            message("question_prompt", self.language),
            self.language,
        )

        choices = []
        for number in range(1, 5):
            choice = read_text(
                message("choice_prompt", self.language, number=number),
                self.language,
            )
            choices.append(choice)

        answer = read_int(
            message("answer_prompt", self.language),
            1,
            4,
            self.language,
        )

        quiz = Quiz(question, choices, answer)
        self.quizzes.append(quiz)

        print(
            message(
                "quiz_added",
                self.language,
                total=len(self.quizzes),
            )
        )

        self.save_state()

    def show_quizzes(self):
        if not self.quizzes:
            print(message("no_quizzes", self.language))
            return

        print()
        print(
            message(
                "quiz_list_title",
                self.language,
                total=len(self.quizzes),
            )
        )
        print("-" * 40)

        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"[{number}] {quiz.question}")

        print("-" * 40)

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
                    self.add_quiz()
                elif choice == 3:
                    self.show_quizzes()
                elif choice == 4:
                    self.show_score()
                elif choice == 5:
                    self.configure_language()
                elif choice == 6:
                    print(message("exit_message", self.language))
                    break

        except KeyboardInterrupt:
            print(message("interrupt", self.language))
        except EOFError:
            print(message("eof", self.language))
        finally:
            self.save_state()


def run_game():
    game = QuizGame()
    game.run()


if __name__ == "__main__":
    try:
        run_game()
    except (OSError, ValueError) as error:
        print(f"언어 설정을 불러오지 못했습니다 / Could not load the language setting: {error}")
        raise SystemExit(1)
