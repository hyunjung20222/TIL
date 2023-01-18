**목차**

1. [모듈](#모듈)
2. [파일](#파일)
   * [파일 읽기](#파일-읽기)
   * [파일 쓰기](#파일-쓰기)
   * [CSV 파일](#csv-파일)
   * [Excel 파일](#excel-파일)

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

---

### CSV 파일

**미디어 타입을 [MIME Type](https://developer.mozilla.org/ko/docs/Web/HTTP/Basics_of_HTTP/MIME_types) 이라고 부른다**

* `xls` 와 `csv` 도 MIME Type 중 하나 (`application/vnd.ms-excel`, `text/csv`)

**CSV**

**첫 번째**

```python
# csv 모듈을 통해서 읽는다
import csv

with open('./resource/sample2.csv', 'r') as f:
    contents = csv.reader(f)
    print(content)
    
# <_csv.reader object at 0x000001F400FA1A20>
# 객체로 지정된다

	print(dir(content))
    # 실행 시 사용 가능한 기능이 나오고, 그 중에 __iter__ 존재 -> 반복 가능
    
    for content in contents:
        print(content)
        # 제대로 나온다
```

* 헤더 Header 없애고 싶을 시

  ```python
  open 한 f 하위에 next(contents) 추가
  ```

**두 번째**

```python
import csv

with open('./resource/sample2.csv', 'r') as f:
    # 옵션자로 나누겠다는 의미로 delimiter 사용
    contents = csv.reader(f, delimiter='|')
    next(contents)
    for content in contents:
        print(content)
```

**세 번째**

* 딕셔너리 형태로 출력

  ```python
  with open('./resource/sample1.csv', 'r') as f:
      contents = csv.DictReader(f)
      print(contents)
  # 출력 시 객체 주소가 나온다 -> 어떤 속성, 메서드를 가지고 있는 지 확인하려면 dir
  ```

  ```python
  # __iter__ 가 있으므로 for 반복문으로 출력
  # 출력 형식이 dict 형태로 나온다
  	for content in contents:
          print(content)
  	# {'번호': '1', '이름': '호식이', '가입일시': '2022-01-19 12:30:00', '나이': '28'}
  ```

  * key 와 value 를 따로 들고 오기

    ```python
    # 비구조화 할당, 순서에 따라 분리해서 할당
    for content in contents:
        for k, v in content.items():
            print(k, ':', v)
        print('----------')
    ```

**네 번째**

* 리스트에서 csv 로 변환

  ```py
  import csv
  
  data = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
  
  with open('./resource/sample3.csv', 'w') as f:
      wt = csv.writer(f)
      # 데이터에 있는 것을 하나씩, 한줄씩 넣어준다
      for content in data:
          wt.writerow(content)
          # 공간이 생긴 채로 파일이 생성된다
          # 1, 2, 3
          #
          # 4, 5, 6
          
          # 이런 식으로
  ```
  
  * 공간을 없애기 위해서는 `newline` 옵션 사용
  
    ```python
    with open('./resource/sample3.csv', 'w', newline='') as f:
        # 공백이 사라진 채 저장된다
        # 1, 2, 3
        # 4, 5, 6
        
        # 이런 식으로
    ```
  
  * `writerows` 를 사용하면 한 줄 씩 인식해서 데이터를 넣어 준다
  
    ```python
    wt.writerows(data)
    ```
  

---

### Excel 파일

```python
# 사전 준비로 설치할 라이브러리
pip install pandas
pip install xlrd
pip install openpyxl
```

**pandas**

```python
# 엑셀 파일 읽는데 사용하는 라이브러리 (인공지능, 머신러닝 등에 사용된다)
import pandas as pd

sample = pd.read_excel('./resource/sample.xlsx')
print(sample)
```

* 데이터 읽을 때 기능

  ```python
  # head
  # 윗 줄 다섯 개 정도 출력해준다
  print(sample.head())
  ```

  ```python
  # shape
  print(sample.shape)
  # (82, 3)
  # 행렬의 각 개수
  ```

  ```python
  # to_[변경할 확장자]
  sample.to_excel('./resource/result.xlsx')
  # result 란 엑셀 파일 생성
  
  sample.to_csv('./resource/result.csv')
  # result 란 csv 파일 생성
  ```

**하지만 pandas 로는 한계가 있다**

&rarr; 그래서 사용하는 라이브러리, **openpyxl**

**openpyxl**

```python
# Workbook 클래스 객체로 파일 생성 가능
from openpyxl import Workbook

# 워크북 생성
wb = Workbook()
# 워크북 저장
wb.save('openpy.xls')
```

* 시트 이름을 정할 수 있다

  ```python
  wb = Workbook()
  ws = wb.active
  # id 라는 이름으로 시트 이름이 생성 된다
  ws.title = 'id'
  wb.save('openpy.xls')
  # 외부 라이브러리이기 때문에 무조건 반환해줘야 한다
  wb.close()
  ```

  







