"""
각 층에 W 개의 방이 있는 H 층 건물이라고 가정하자 (1 ≤ H, W ≤ 99).
그리고 엘리베이터는 가장 왼쪽에 있다고 가정하자
이런 형태의 호텔을 H × W 형태 호텔이라고 부른다.
호텔 정문은 일층 엘리베이터 바로 앞에 있는데, 정문에서 엘리베이터까지의 거리는 무시한다.
또 모든 인접한 두 방 사이의 거리는 같은 거리(거리 1)라고 가정하고 호텔의 정면 쪽에만 방이 있다고 가정한다.

방 번호는 YXX 나 YYXX 형태인데 여기서 Y 나 YY 는 층 수를 나타내고
XX 는 엘리베이터에서부터 세었을 때의 번호를 나타낸다
걷는 거리가 같을 때에는 아래층의 방을 더 선호한다

여러분이 작성할 프로그램은 초기에 모든 방이 비어있다고 가정하에
이 정책에 따라 N 번째로 도착한 손님에게 배정될 방 번호를 계산하는 프로그램이다.
"""

# 높이가 1일 때 예외처리
# 주어진 높이가 최대일 때 (= 나머지가 0일 때, 몫이 0일 때) 예외처리

import sys
T = int(sys.stdin.readline())
for tc in range(T):
    H, W, N = map(int, sys.stdin.readline().split())

    new_H = N % H
    new_W = N // H + 1

    if H == 1:
        new_H += 1
        new_W -= 1

    if not new_H:
        new_H = H
        new_W -= 1

    if new_W < 10:
        print("".join([str(new_H), "0", str(new_W)]))
    else:
        print("".join([str(new_H), str(new_W)]))