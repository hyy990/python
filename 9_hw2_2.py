topAvg=topName=None
bottomAvg=bottomName=None
topEng=topEngName=None
topMath=topMathName=None
bottomEng=bottomEngName=None
bottomMath=bottomMathName=None

n=int(input("학생수 입력: "))

print("\n%d번째 학생 성적처리"%1)

name = input("이름: ")
eng = int(input("영어 성적: ")) ;  math = int(input("수학 성적: "))
total = eng + math ;  avg = total / 2

if avg>=90 :  grade = 'A'
elif avg>=80 :  grade = 'B'
elif avg>=70 :  grade = 'C'
elif avg>=60 :  grade = 'D'
else :  grade =  'F'

print("-"*55)
print(" 이  름\t\t영어\t수학\t총점\t평균\t학점")
print("-"*55)
print (" %s\t\t%3d\t%3d\t%3d\t%.2f\t%2c" % (name, eng, math, total, avg, grade))
print("-"*55)

topAvg = bottomAvg= avg; topName = bottomName = name
topEng = bottomEng= eng; topEngName = bottomEngName = name
topMath = bottomMath = math ; topMathName = bottomMathName = name

for i in range(2,n+1):
    print("\n%d번째 학생 성적처리" %i)
    name = input("이름: ")
    eng = int(input("영어 성적: ")) ;  math = int(input("수학 성적: "))
    total = eng + math ;  avg = total / 2

    if avg>=90 :  grade = 'A'
    elif avg>=80 :  grade = 'B'
    elif avg>=70 :  grade = 'C'
    elif avg>=60 :  grade = 'D'
    else :  grade =  'F'
    print("-"*55)
    print(" 이  름\t\t영어\t수학\t총점\t평균\t학점")
    print("-"*55)
    print (" %s\t\t%3d\t%3d\t%3d\t%.2f\t%2c" % (name, eng, math, total, avg, grade))
    print("-"*55)

    if topAvg < avg:
       topAvg = avg; topName = name
    if bottomAvg > avg:
       bottomAvg = avg; bottomName = name
    if topEng < eng:
       topEng = eng; topEngName = name
    if bottomEng > eng:
       bottomEng = eng; bottomEngName = name
    if topMath < math:
       topMath = math; topMathName = name
    if bottomMath > math:
       bottomMath = math; bottomMathName = name
    

print("\n영어최고득점 : %s, 점수: %3d" %(topEngName, topEng))
print("\n수학최고득점 : %s, 점수: %3d" %(topMathName, topMath))
print("\n영어최저득점 : %s, 점수: %3d" %(bottomEngName, bottomEng))
print("\n수학최저득점 : %s, 점수: %3d" %(bottomMathName, bottomMath)) 
print("\n최고평균: %6.2f(%s)" %(topAvg, topName))
print("\n최저평균: %6.2f(%s)" %(bottomAvg, bottomName))


