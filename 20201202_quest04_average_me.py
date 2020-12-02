ko = int(input("국어점수를 입력하세요 : "))
ma = int(input("수학점수를 입력하세요 : "))
en = int(input("영어점수를 입력하세요 : "))

add = 0
for i in [ko, ma, en] :     
    add = add + i
print("총점은 %d 이며 평균은 %.1f 입니다." % (add, add/3))
