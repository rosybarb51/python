def is_odd(number):
    if int(number) % 2 == 0:
        return True
    else :
        return False
while True :
    number = input("숫자를 입력하세요.\n (종료시 quit 또는 exit)\n: ")
    if number in ['quit', 'exit'] :
        print("\n프로그램을 종료합니다.\n")
        break

    result = is_odd(number)

    if result == True :
        print("\n짝수입니다.\n")
    else :
        print("\n홀수입니다.\n")
