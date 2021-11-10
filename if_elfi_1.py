a = int(input('당신의 중간고사 성적을 입력하시오'))

if a>=90:
    print(f'{a}점수는 A학점에 해당합니다.')
elif a>=80:
    print(f'{a}점수는 B학점에 해당합니다.')

elif a>=70:
    print(f'{a}점수는 C학점에 해당합니다.')

elif a>=60:
    print(f'{a}점수는 D학점에 해당합니다.')

else:
    print(f'{a}점수는 축하드립니다. 계절학기 당첨되셨습니다.')
b = int(input("점수입력"))

res=''
if a>=60:
    res = '합격'
else:
    res='불합격'
    print(res)

    res='합격' if a>=60 else'불합격'
    