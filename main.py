def read_int(prompt, min_value, max_value):
    while True:
        text = input(prompt).strip()

        if text == "":
            print("입력이 비어 있습니다. 숫자를 입력하세요.")
            continue

        try:
            number = int(text)
        except ValueError:
            print("숫자로 바꿀 수 없습니다. 정수를 입력하세요.")
            continue

        if not min_value <= number <= max_value:
            print(f"{min_value}~{max_value} 사이의 숫자를 입력하세요.")
            continue

        return number


def show_menu():
    print()
    print("=" * 40)
    print("나만의 퀴즈 게임")
    print("=" * 40)
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")
    print("=" * 40)


def run_game():
    while True:
        show_menu()
        choice = read_int("선택: ", 1, 5)

        if choice == 1:
            print("퀴즈 풀기를 선택했습니다. 구현 예정입니다.")
        elif choice == 2:
            print("퀴즈 추가를 선택했습니다. 구현 예정입니다.")
        elif choice == 3:
            print("퀴즈 목록을 선택했습니다. 구현 예정입니다.")
        elif choice == 4:
            print("점수 확인을 선택했습니다. 구현 예정입니다.")
        elif choice == 5:
            print("퀴즈 게임을 종료합니다.")
            break


if __name__ == "__main__":
    try:
        run_game()
    except KeyboardInterrupt:
        print("\nCtrl+C를 감지했습니다. 프로그램을 종료합니다.")
    except EOFError:
        print("\n입력이 종료되었습니다. 프로그램을 종료합니다.")