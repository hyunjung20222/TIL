"""
점의 좌표를 입력받아 그 점이 어느 사분면에 속하는지 알아내는 프로그램을 작성하시오.
단, x 좌표와 y 좌표는 모두 양수나 음수라고 가정한다.

첫 줄에는 정수 x가 주어진다. (−1000 ≤ x ≤ 1000; x ≠ 0) 다음 줄에는 정수 y가 주어진다. (−1000 ≤ y ≤ 1000; y ≠ 0)
점 (x, y)의 사분면 번호(1, 2, 3, 4 중 하나)를 출력한다.
"""

import sys
sys.stdin = open('input.txt', 'r')

X = int(input())
Y = int(input())

"""
구현방법 1 : 틀렸습니다!

당연히 틀리는 게 음수가 False 가 아니다! 0이 False 인거지..
"""
# # 1 사분면과 3 사분면
# if X and Y:
#     if X > 0:
#         print(1)
#     else:
#         print(3)
# # 2 사분면과 4 사분면
# else:
#     if X < 0:
#         print(2)
#     else:
#         print(4)
"""
구현방법 2
"""
if X > 0:
    if Y > 0:
        print(1)
    else:
        print(4)
else:
    if Y > 0:
        print(2)
    else:
        print(3)