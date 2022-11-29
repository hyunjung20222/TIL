"""
셀프 넘버는 1949년 인도 수학자 D.R. Kaprekar가 이름 붙였다.
양의 정수 n에 대해서 d(n)을 n과 n의 각 자리수를 더하는 함수라고 정의하자.
예를 들어, d(75) = 75+7+5 = 87이다.

양의 정수 n이 주어졌을 때, 이 수를 시작해서 n, d(n), d(d(n)), d(d(d(n))), ...과 같은 무한 수열을 만들 수 있다.
n을 d(n)의 생성자라고 한다
생성자가 없는 숫자를 셀프 넘버라고 한다

10000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
"""

cnt = 1
numlist = []
for n in range(1, 10000):
    numlist.append(n)

def checknum(n):
    ans = n
    for i in str(n):
        ans += int(i)
    return ans

"""
remove() 는 값을 입력받아서 지우는 것
pop(), del() 은 인덱스 입력받아서 지우고 인덱스 반환 / 반환하지 않음
"""

while cnt < 10000:
    num = checknum(cnt)
    if num in numlist:
        numlist.remove(num)
        cnt += 1
        checknum(cnt)
    else:
        cnt += 1
        checknum(cnt)

for k in numlist:
    print(k)
