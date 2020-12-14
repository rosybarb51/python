def is_odd(number):
    if int(number) %2 == 0:
        return True
    else:
        return False
while True :
    number = input("숫자 입력: ")

    if number in ['exit','quit']:
        print("프로그램 종료")
        break

    result = is_odd(number)

    if result == True : print("짝수")
    else : print("홀수")
    
