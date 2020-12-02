start = int(input("시작 숫자 : "))
end = int(input("끝 숫자 : "))

i = start
sum = 0
while i<= end :
    sum += i
    i+= 1

print ("%d에서 %d까지 합은 %d입니다." % (start, end, sum))
