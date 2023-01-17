**목차**

1. [모듈](#모듈)
2. [파일](#파일)

---

## 모듈

**기능 단위로 구분 되어진 파일 뭉치 (라이브러리와 유사)**

* 패키지
  * 모듈을 모아둔 디렉터리로, python 의 경우 pip 이라는 package manager 존재
  * 설치 방법 : pip install [패키지 or 모듈명]
* 외부에서 모듈 사용 시 import 문 사용



**사용 예시 1**

```python
import inspect
import random

print(inspect.getfile(random))

# C:\Users\User\AppData\Local\Programs\Python\Python310\lib\random.py
# bash 창에서 cat -n [경로] 로 확인
```



**사용 예시 2**

* `pkg/Calculator.py` 에 모듈 (클래스) 작성

```python
class Calculator:
    def __init__(self, title):
        self.title = 'Cal module'
        
    def plus(x, y):
        return x + y
    
    def minus(x, y):
        return x - y
```

* import 를 통해 `01_module.py` 에서 사용

  ```python
  from pkg.Calculator import Calculator
  
  print(Calculator.plus(1, 4))
  print(Calculator.minus(1, 4))
  ```

  *  `from pkg.Calculator import *` 해도 동작하나 지양 
    * 사용하지 않을 것 다 가져올 필요 없다
  * `from pkg.Calculator import Calculator as cal` 이면 cal 로 별칭 지정하는 것



**사용 예시 3**

* `pkg/calculator2.py` 에 모듈 (함수) 작성 후 import

```python
def plus(x, y):
    return x + y

def minus(x, y):
    return x - y
```

* import 한 부분

  ```python
  from pkg.calculator2 import plus
  
  print(plus(1, 4))
  ```

---



## 파일

| 종류 | 설명                                                    |
| ---- | ------------------------------------------------------- |
| `r`  | 읽기                                                    |
| `w`  | 쓰기                                                    |
| `a`  | 파일이 존재하지 않을 시 만들고, 아니라면 덧붙인다 (add) |

### 파일 읽기

**첫 번째**

```python
open(읽어올 파일 경로, 수행할 모드)
```

* 예시

  ```python
  f = open('./resource/python.txt', 'r')
  print(f)
  # <_io.TextIOWrapper name='./resource/python.txt' mode='r' encoding='cp949'>
  
  # 내용 읽기
  contents = f.read()
  print(contents)
  # 파일 내부 내용이 출력 된다
  
  # 외부 자원을 사용했으면 다시 돌려줘야 한다
  f.close()
  ```

**두 번째**

```python
with open(읽어올 파일 경로, 수행할 모드) as f
```

* 예시

  ```python
  with open('./resource/python.txt', 'r') as f:
      contents = f.read()
      print(contents)
      
      # iterable 한 파일 읽고, 리스트로 만들고
      iter(contents)
      list(contents)
  ```

  * 외부 자원을 사용한 후에 자동으로 close 해주므로 close 를 지정할 필요 없음



**read()** 는 한 번에 다 읽어오므로 한 줄로 읽어오는 것이 불가능

* `readline()` , `readlines()` 사용 
  * 한 줄 씩 읽거나, 전체 내용을 읽은 뒤에 줄 단위로 리스트로 가져와서 출력 

```python
with open('./resource/python.txt', 'r') as f:
    contents = f.readlines()
    print('>>>', contents)
# >>> ['Python is powerful... and fast;\n', 'plays well with others;\n', 'runs everywhere;\n', 'is friendly & easy to learn;\n', 'is Open.']
# 반복문 통해 한 줄씩 출력 가능

# print(contents, end='') end 에 할당된 값이 붙은채로 출력
```

### 파일 쓰기

**첫 번째**

```python
with open(저장할 경로, 'w') as f:
    f.write(저장할 내용)
```

* 예시

  ```python
  with open('./resource/info.txt', 'w') as f:
      f.write('nice day!')
  ```

  * 경로에 `info.txt` 라는 파일이 생성된다 &rarr; nice day 생성

  ```python
  with open('./resource/info.txt', 'a') as f:
      f.write('nice day!')
  ```

  * 이미 만든 `info.txt` 파일에 새롭게 추가 (add)
    * nice day!nice day! 가 됨

**두 번째**

* `writelines()` 라인을 기준으로 저장

  ```python
  with open('./resource/info2.txt', 'a') as f:
      f.writelines('nice day!\nnice day!\nnice day!')
  ```

  ```python
  # info2.txt 에 라인별로 제대로 저장 된다
  nice day!
  nice day!
  nice day!
  ```

**파일 생성 시 기존에 파일이 있었다면 덮어쓰기 되므로 주의**

**세 번째**

파일로 바로 저장하는 법

```python
with open('./resource/info3.txt', 'w') as f:
    print('freedom', file=f)
```

* print 하고 file 이란 옵션을 주면 새로이 파일이 생성된다