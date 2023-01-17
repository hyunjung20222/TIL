## 문제 1

우리나라의 주민등록번호는 뒷자리 첫 번째 자리 숫자를 가지고 남성(1, 3)과 여성(2, 4)을 구분합니다. 이를 구분하는 프로그램을 만들어 주세요.

- 예) serial_no = '871025-1234567' &rarr;  남성입니다.

```python
# 남성 여성을 구분하는 함수
def ckmfm(point):
  if point in [1, 3]:
    print("남성입니다")
  elif point in [2, 4]:
    print("여성입니다")
  else:
    print("잘못 입력했습니다. 다시 입력해주세요.")
    ckright(num = input('재입력 : '))

# 제대로 입력했는지 확인하는 함수
def ckright(num):
  try:
    lst = num.split('-')
    if len(lst[1]) == 7:
      try:
        ckpoint = int(lst[1][0])
        ckmfm(ckpoint)
      except:
        print("잘못 입력했습니다. 다시 입력해주세요.")
        ckright(num = input('재입력 : '))
    else:
      print("잘못 입력했습니다. 다시 입력해주세요.")
      ckright(num = input('재입력 : '))
  except:
    print("잘못 입력했습니다. 다시 입력해주세요.")
    ckright(num = input('재입력 : '))

ckright(num = input('주민등록번호를 입력해주세요. : '))
```



## 문제 2

\# +, -, * / 기본 사칙 연산에 대한 결과 값을 반환하는 함수

```python
# 숫자 외의 문자를 입력했을 때 에러 
def catch_error(num):
  try:
    return int(num)
  except:
    print("잘못 입력했습니다. 숫자를 입력해주세요!")
    return get_num()

# 숫자 입력받는 함수
def get_num():
  ckpoint = (input('종료 시 quit 을, 시작 시 start 를 입력해주세요 : '))
  if ckpoint == 'quit':
    print("종료됐습니다.")
    return
  elif ckpoint == 'start':
    a = input('첫번째 숫자 입력 : ')
    a = catch_error(a)
    b = input('두번째 숫자 입력 : ')
    b = catch_error(b)
    return operator(a, b)
  else:
    ckpoint = input('제대로 입력해주세요! : ')
    get_num()

def operator(a, b):
  opt = input('+, -, /, * 중 하나를 입력해주세요 : ')
  if opt == '+':
    print(f'답은 {a + b} 입니다.')
    return get_num()
  elif opt == '*':
    print(f'답은 {a * b} 입니다.')
    return get_num()
  elif opt == '/':
    print(f'답은 {a / b} 입니다.')
    return get_num()
  elif opt == '-':
    print(f'답은 {a - b} 입니다.')
    return get_num()
  else:
    print("잘못 입력하셨습니다. 다시 입력해 주세요.")
    return operator(a, b)

get_num()
```



## 단축키

`ctrl + \` 창 나누기

`ctrl + B` 옆 파일 창 없애기

`alt + 클릭` 여러 개 동시에 선택

