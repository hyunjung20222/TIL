"""
그룹 단어란 단어에 존재하는 모든 문자에 대해서,
각 문자가 연속해서 나타나는 경우만을 말한다. 예를 들면, ccazzzzbb 는 c, a, z, b가 모두 연속해서 나타나고,
kin 도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, aabbbccb 는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

첫째 줄에 단어의 개수 N이 들어온다.
N은 100보다 작거나 같은 자연수이다.
둘째 줄부터 N개의 줄에 단어가 들어온다.
단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.
"""

T = int(input())
senlist = []

for tc in range(1, T+1):
    sentence = input()
    senlist.append(sentence)

# 초기값
ans = 0

for sen in senlist:
    charlist = []
    flag = True
    for i in range(len(sen)):
        if not i:
            charlist.append(sen[i])
        else:
            if sen[i] in charlist and sen[i] != charlist[i - 1]:
                flag = False
                break
            else:
                charlist.append(sen[i])
    if flag:
        ans += 1
print(ans)


