**목차**

1. [예외](#예외)
   * [종류](#종류)
2. [예외 처리](#예외-처리)

---

## 예외

**코드 실행 시 발생할 수 있는 문제**

* Error 와의 차이점
  * Error 는 시스템 상에서 발생하는 문제로, 개발자가 해결할 수 없는 경우를 의미

### 종류

* **Syntax**

  * 문법적 에러

  ```python
  # SyntaxError: unterminated string literal (detected at line 1)
  print('python )
  ```

* **Name**

  * 참조 변수가 초기화되지 않거나 존재하지 않는 예외

  ```python
  # NameError: name 'a' is not defined
  print(a)
  ```

* **ZeroDivisionError**

  ```python
  # ZeroDivisionError: division by zero
  print(10 / 0)
  ```

* **Index**

  * 존재하지 않는 인덱스를 참조할 때 발생하는 예외

  ```python
  # IndexError: list index out of range
  a = [1, 2, 3]
  print(a[3])
  
  # IndexError: pop from empty list
  a = []
  a.pop()
  ```

* **Key** 

  * 딕셔너리에서 key 가 존재하지 않을 때 발생하는 예외

  ```python
  # None
  # 예외는 발생하지 않는다
  dict1 = {'name': 'lhj', 'id' : 1234, 'city' : 'seoul'}
  print(dict1.get('age'))
  
  # KeyError: 'age'
  dict1 = {'name': 'lhj', 'id' : 1234, 'city' : 'seoul'}
  print(dict1['age'])
  ```

  * `get` 을 쓰는 것을 권장 
    * 예외가 발생하지 않는 함수를 사용할 것!

* **Attribute**

  * 모듈, 클래스에 없는 속성을 사용할 때 발생하는 예외

  ```python
  # AttributeError: module 'time' has no attribute 'clock'
  import time
  print(time.clock())
  ```

* **Value**

  * 참조 값이 존재하지 않을 때 발생하는 예외

  ```python
  # ValueError: 4 is not in list
  a = [1, 2, 3]
  a.index(4)
  
  # index() 는 파라미터로 받은 값과 동일한, 첫번째로 있는 값의 인덱스를 반환
  
  # ValueError: list.remove(x): x not in list
  a.remove(4)
  # 리스트에 존재하지 않는 값을 삭제하기 때문에 ValueError 발생
  ```

* **FileNotFound**

  * 존재하지 않는 파일 사용 시 발생하는 예외

  ```python
  # FileNotFoundError: [Errno 2] No such file or directory: './test.txt'
  f = open('./test.txt', 'r') 
  ```

* **Type**

  * 데이터 타입에 알맞지 않은 연산 시 발생하는 예외

  ```python
  # TypeError: can only concatenate str (not "int") to str
  print('a' + 3)
  ```

---

## 예외 처리

```python
try:
    수행 코드
except 예외명:
    예외 처리 수행 코드
else:
    예외 발생하지 않는 경우 수행되는 코드
finally:
    항상 수행되는 코드
```

* 예시

  ```python
  # 특정 성의 위치를 출력하는 기능
  last_names= ['lee', 'park', 'kim']
  
  # 존재하지 않는 성이 있을 경우 예외 처리
  try:
      search_name = 'jung'
      idx = last_names.index(search_name)
      print(f'{search_name} 은 {idx + 1} 번 째에 위치하고 있습니다.')
  except ValueError:
      print('검색하신 last name 은 존재하지 않습니다')
  ```

  ```python
  # 무조건 처리해야할 경우
  try:
      print('try')
  finally:
      print('finally')
  ```

* 예외 명 발생 시킬 때 쓰는 키워드

  ```python
  raise [예외명]
  ```

  * 예시

    ```python
    # bae 를 찾지 못했습니다. 출력
    try:
        last_name = 'lee'
        if last_name == 'bae':
            print('bae 를 찾았습니다.') 
        else:
            raise ValueError
    except ValueError:
        print("bae 를 찾지 못했습니다.")
    ```

* 모든 예외 다 처리하는 클래스

  * 제일 마지막에 사용

  ```python
  except ValueError:
      ValueError 일 때 수행하는 코드
  except Exception:
      ValueError 가 아닌 나머지 예외 코드를 전부 처리하는 클래스
  ```

* 예외를 직접 만들어서 사용할 수 있다

  ```python
  class NotFoundParkError(Exception):
      print("사용자 정의 에러입니다.")
  # except NotFoundParkError 사용 가능
  ```

