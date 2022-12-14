"""
알파벳 소문자로만 이루어진 단어 S가 주어진다.
각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를,
포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

각각의 알파벳에 대해서, a가 처음 등장하는 위치, b가 처음 등장하는 위치, ... z가 처음 등장하는 위치를 공백으로 구분해서 출력한다.
만약, 어떤 알파벳이 단어에 포함되어 있지 않다면 -1을 출력한다.
단어의 첫 번째 글자는 0번째 위치이고, 두 번째 글자는 1번째 위치이다.
"""

arr = input()
alphalist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
anslist = []
"""
문자열 찾는 방법
두 방법 다 처음으로 나온 문자의 index 값을 반환한다
find() : 찾는 값이 없는 경우 -1 출력 / 문자열만 사용 가능하며 리스트, 튜플, 딕셔너리에서는 사용할 수 없다
index() : 찾는 값이 없는 경우 ValueError / 딕셔너리 자료형에 사용할 수 없다
"""
for char in alphalist:
    ans = arr.find(char)
    print(ans, end=' ')
