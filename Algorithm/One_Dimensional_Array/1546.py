"""
세준이는 자기 점수 중에 최댓값을 골랐다.
이 값을 M 이라고 한다. 그리고 나서 모든 점수를 점수 / M * 100으로 고쳤다

세준이의 성적을 위의 방법대로 새로 계산했을 때, 새로운 평균을 구하는 프로그램을 작성하시오.

첫째 줄에 시험 본 과목의 개수 N이 주어진다.
이 값은 1000보다 작거나 같다.
둘째 줄에 세준이의 현재 성적이 주어진다.
이 값은 100보다 작거나 같은 음이 아닌 정수이고, 적어도 하나의 값은 0보다 크다.
"""

import sys

N = int(input())
scorelist = list(map(int, sys.stdin.readline().split()))

ans = sum(scorelist) / max(scorelist) * 100 / N
print(ans)