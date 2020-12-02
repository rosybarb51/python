def is_odd(number):
    if int(number) % 2 == 0 :
        return True
    else :
        return False
while True :
    number = input("숫자를 입력하세요 : ")
    if number in ['quit','exit']:
        print("프로그램을 종료합니다.")
        break

    result = is_odd(number)
    if result == True :
        print("짝수입니다.")
    else :
        print("홀수입니다.")
