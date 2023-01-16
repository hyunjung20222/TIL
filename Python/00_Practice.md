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



