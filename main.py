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
        choice = input("선택: ").strip()

        if choice == "1":
            print("퀴즈 풀기를 선택했습니다. 구현 예정입니다.")
        elif choice == "2":
            print("퀴즈 추가를 선택했습니다. 구현 예정입니다.")
        elif choice == "3":
            print("퀴즈 목록을 선택했습니다. 구현 예정입니다.")
        elif choice == "4":
            print("점수 확인을 선택했습니다. 구현 예정입니다.")
        elif choice == "5":
            print("퀴즈 게임을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 1~5 중 하나를 입력하세요.")


if __name__ == "__main__":
    run_game()