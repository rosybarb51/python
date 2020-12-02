def is_odd(number):
    if int(number) % 2 == 0:
        return True
    else:
        return False
while True :
    number = input("숫자를 입력하세요. \n(종료시 quit이나 exit 입력) \n: ")

    if number in ['exit','EXIT','quit']:
        print("\n프로그램을 종료합니다.\n")
        break

    result = is_odd(number)

    if result == True : print("\n=>짝수입니다.\n")
    else : print("\n=>홀수입니다.\n")
    
