"""
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
단, 대문자와 소문자를 구분하지 않는다.
"""

# 문자열에서 특정 문자 개수 세기 : count()

char = input()
alphadict = {
    0: ['a', 'A'],
    1: ['b', 'B'],
    2: ['c', 'C'],
    3: ['d', 'D'],
    4: ['e', 'E'],
    5: ['f', 'F'],
    6: ['g', 'G'],
    7: ['h', 'H'],
    8: ['i', 'I'],
    9: ['j', 'J'],
    10: ['k', 'K'],
    11: ['l', 'L'],
    12: ['m', 'M'],
    13: ['n', 'N'],
    14: ['o', 'O'],
    15: ['p', 'P'],
    16: ['q', 'Q'],
    17: ['r', 'R'],
    18: ['s', 'S'],
    19: ['t', 'T'],
    20: ['u', 'U'],
    21: ['v', 'V'],
    22: ['w', 'W'],
    23: ['x', 'X'],
    24: ['y', 'Y'],
    25: ['z', 'Z'],
}

maxValue = 0
ans = ''

# 딕셔너리에서 .get(key) 를 쓰면 value 값 출력 가능

for n in range(26):
    cnt = char.count(alphadict.get(n)[0]) + char.count(alphadict.get(n)[1])
    if cnt > maxValue:
        maxValue = cnt
        ans = alphadict.get(n)[1]
    elif cnt == maxValue and cnt != 0:
        ans = '?'
    else:
        pass
print(ans)