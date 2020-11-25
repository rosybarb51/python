## readline 사용하기

## readline으로 첫 줄만 출력하기

##f = open("C:/python102/새파일.txt",'r')
##line = f.readline()
##print(line)
##f.close()

## readline과 while 문으로 모든 줄 출력하기

##f = open("C:/python102/새파일.txt",'r')
##while True:
##    line = f.readline()
##    if not line: break
##    print(line)
##f.close()


## readlines 사용하기

##f = open("C:/python102/새파일.txt", 'r')
##lines = f.readlines()
##for line in lines:
##    print(line)
##f.close()


## read 함수 사용하기

##f = open("C:/python102/새파일.txt", 'r')
##data = f.read()
##print(data)
##f.close()


## 파일에 새로운 내용 추가하기

##f = open("C:/python102/새파일.txt", 'a')
##for i in range(11, 20) :
##    data = "%d 번째 줄입니다.\n" % i
##    f.write(data)
##f.close()


## with문과 함께 사용하기

##with open("file01.txt", "w") as f :
##    f.write("Life is too short, you need python!")


## p180 연습문제 7)

##f = open('file02.txt', 'r')
##body = f.read()
##f.close()
##
##body = body.replace("python","sugar")
##
##f = open('file02.txt', 'w')
##f.write(body)
##f.close()

##7번 문제 readlines로 읽었을 때 파일 내용 바꾸기 (강사님)
##파일에 있는 것을 메모리에 올리고, 다시 파일로 내리는 과정 
##
##f = open("C:/python102/python/file02.txt",'r')
##lines = f.readlines()
##f.close()
##
##f = open("C:/python102/python/file02.txt",'w')
##for line in lines:
##    line = line.replace("sugar", "python")
##    f.write(line)
##f.close()


## 연습문제 5)

##f1 = open("test.txt", 'w')
##f1.write("Life is too short")
##f1.close()
##
##f2 = open("test.txt", 'r')
##print(f2.read())
##f2.close()

## 연습문제 6)

##user_input = input("저장할 내용을 입력하세요: ")
##f = open('test.txt', 'a')
##f.write(user_input)
##f.write("\n")
##f.close()










