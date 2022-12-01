"""
단어가 주어졌을 때, 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.
위 목록에 없는 알파벳은 한 글자씩 센다.

첫째 줄에 최대 100글자의 단어가 주어진다. 알파벳 소문자와 '-', '='로만 이루어져 있다.
단어는 크로아티아 알파벳으로 이루어져 있다.
문제 설명의 표에 나와있는 알파벳은 변경된 형태로 입력된다.

입력으로 주어진 단어가 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.
"""

# 한 개로 세는 크로아티아 알파벳
# 구현 방법 1 : 틀렸습니다!
"""
alphalist = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

sentence = input()
cnt = len(sentence)

for alpha in alphalist:
    newsen = sentence
    num = sentence.count(alpha)
    if num:
        sentence = sentence.replace(alpha, ' ')
        print(sentence)
    cnt -= (len(alpha) - 1) * num
print(cnt)
"""

# 구현 방법 2
alphalist = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for alpha in alphalist:
    word = word.replace(alpha, "*")
print(len(word))