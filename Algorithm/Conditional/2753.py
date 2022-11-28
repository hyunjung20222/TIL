"""
연도가 주어졌을 때, 윤년이면 1, 아니면 0을 출력하는 프로그램을 작성하시오.

윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.
예를 들어, 2012년은 4의 배수이면서 100의 배수가 아니라서 윤년이다.
1900년은 100의 배수이고 400의 배수는 아니기 때문에 윤년이 아니다.
하지만, 2000년은 400의 배수이기 때문에 윤년이다.

첫째 줄에 연도가 주어진다. 연도는 1보다 크거나 같고, 4000보다 작거나 같은 자연수이다.
첫째 줄에 윤년이면 1, 아니면 0을 출력한다.
"""

import sys
sys.stdin = open('input.txt', 'r')

nowyear = int(input())

"""
구현방법 1 : 틀렸습니다!

세 조건 모두 True 거나 False 일 경우에도 True 로 결과가 나오므로 예외 처리 안됨
"""
# if not nowyear % 4 and not nowyear % 400 or nowyear % 100:
#     print('1')
# else:
#     print('0')

"""
구현방법 2

예외 처리가 가능하도록 일일히 조건을 줬다
"""
if not nowyear % 4:
    if not nowyear % 400:
        print(1)
    elif nowyear % 100:
        print(1)
    else:
        print(0)
else:
    print(0)