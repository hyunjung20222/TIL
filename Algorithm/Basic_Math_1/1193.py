"""
나열된 분수들을 1/1 → 1/2 → 2/1 → 3/1 → 2/2 → … 과 같은 지그재그 순서로
차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.

X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.
"""

import sys
X = int(sys.stdin.readline())

flag = True
cnt = 1

while flag:
    if X <= cnt * (cnt + 1) / 2:
        c = int(X - cnt * (cnt - 1) / 2)
        m = int(cnt + 1 - c)
        # 지그재그이므로 순서도 바뀐다
        if not cnt % 2:
            print("".join([str(c), "/", str(m)]))
        else:
            print("".join([str(m), "/", str(c)]))
        flag = False
    else:
        cnt += 1
