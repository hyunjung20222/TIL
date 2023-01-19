**목차**

1. [데이터 구조](#데이터-구조)
   * [시퀀스 자료형](#시퀀스-자료형)
   * [집합 자료형](#집합-자료형)
   * [매핑 자료형](#매핑-자료형)
2. [함수](#함수)
3. [객체와 클래스](#객체와-클래스)
   * [클래스](#클래스)
   * [객체](#객체)

---

## 데이터 구조

**데이터를 효율적으로 나타내기 위한 데이터 타입**

### 시퀀스 자료형

**튜플**

* 리스트와 동일하게 목록 형태로 데이터를 관리하는 자료형

* 데이터 나열 순서 존재, 수정 불가능

  ```python
  튜플 변수명 = ( 데이터 1, 데이터 2, ... )
  ```

  

### 집합 자료형

**집합**

* 집합을 처리하기 위해 사용되는 자료형

* 데이터 나열 순서 존재 하지 않음, 중복 불가능

  * 순서가 없기 때문에 인덱싱 할 수 없다

  ```python
  집합 변수명 = set( 반복 가능한 객체	)
  집합 변수명 = { 데이터 1, 데이터 2, ...}
  # iterable 한 객체로, 내부의 데이터를 하나씩 꺼내 올 수 있고 반복 시 종료할 수 있는 내부 반환값을 제공하는 객체
  # list, dict, set, str, bytes, tuple, range
  ```

  * 예시

    ```python
    set1 = {'가', '나', '다'}
    set2 = set([1, 1, 2, 1, 2, 3])
    # print(set2)
    # {1, 2, 3}
    ```

* 데이터 추가

  * `add()` 집합에 하나의 데이터 (숫자, 문자열, 튜플) 만 추가

    ```python
    set3 = {1, 2, 3, 4, 5}
    set3.add(6)
    # {1, 2, 3, 4, 5, 6}
    ```

  * `update(*others)` 집합에 여러 개의 값을 추가

    * 마찬가지로 iterable 한 객체를 추가해야 한다

    ```python
    set3.update([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    ```

* 데이터 삭제
  * `remove(elem)` 집합에서 지정 요소 삭제하며 요소가 없을 경우 Error 발생
  * `discard(elem)` 집합에서 지정 요소 삭제하며 요소가 없을 경우에도 Error 발생하지 않음
* 합집합, 교집합, 차집합
  * `.union()` or`|` 합집합
  * `.intersection()` or`&` 교집합
  * `.difference()` or `-` 차집합



### 매핑 자료형

**딕셔너리**

* 키와 값 (key, value) 을 한 쌍으로 갖는 자료형

  * 키 (key) 는 **고유한 값** &rarr; 수정 불가능

* 키를 통해 값을 반환 받을 수 있다

  ```python
  딕셔너리 변수명 = dict([('one', 1), ('two', 2), ... ])
  딕셔너리 변수명 = { key1 : Value1, Key2 : Value2, ... }
  ```

  * 내부 값 추출

    * `[key]` or `.get(key)` 

    * `keys()` 딕셔너리 키만 `dict_keys` 객체로 반환

    * `values()` 딕셔너리의 값만 `dict_values` 객체로 반환

    * `items()` 딕셔너리의 키, 값 쌍으로 `dict_items` 반환

      ```python
      dict0 = {'a' : 1, 'b' : 2, 'c' : 3}
      
      dict0.keys()
      # dict_keys(['a', 'b', 'c'])
      dict0.values()
      # dict_values([1, 2, 3])
      dict0.items()
      # dict_items([('a', 1), ('b', 2), ('c', 3)])
      ```

      * 키 존재 여부 확인

        ```python
        [찾고 싶은 키 값] in dict0.keys()
        ```

* 수정 및 삭제

  * `[key] = new 데이터` 

    ```python
    dict1 = {'apple': 3, 'banana': 9}
    dict1['orange'] = 1
    # {'apple': 3, 'banana': 9, 'orange': 1}
    ```

  * `del [key]` 

    ```python
    del dict1['apple']
    # {'banana': 9, 'orange': 1}
    ```

    

---

## 함수

**특정 기능을 수행할 수 있는 코드 구문**

* 기능 별로 코드를 구분할 수 있도록 만들 수 있다
* 반복적인 코드 작성을 최소화해 목표 기능 수행 가능 &rarr; 재사용성이 좋다
* 필요 기능에 따라 새로운 함수 정의 가능

```python
def 함수명([매개변수 parameter, ... ]):
	수행 코드
    ...
    [return 반환값]
```

* 함수는 `함수명(매개변수)` 로 호출하면 된다
* `[]` 는 옵션값이라는 의미 

```python
# return 값이 없는 경우, 이는 print 라는 기능이 함수에 정의된 것
def hello1():
	print("Hello, Python")
    
# return 값이 있는 경우, 이는 return 값이 함수에 정의된 것
# 외부 전달을 위해서는 return 이 있어야 한다
def hello2():
    return "Hello, Python"

# 매개변수가 있는 경우
def hello3(language):
    return 'Hello,' + ' ' + language
```

* 함수에 초기 값 설정 가능

  ```python
  def print_name(name, id="1234"):
      return name + ' ' + id
  ```

* 다중매개변수

  * `*` 는 0 ~ 무한대의 매개 변수 개수를 가리킨다

  ```python
  def print_data(*args):
    print(args)
  
  # print_data(1, 2, 3) -> (1, 2, 3) 으로 튜플이 출력됨
  ```

* 키워드 매개변수

  * 키와 값 한 쌍으로 구성 돼 있는 데이터 형식

  ```python
  def print_data2(**kwargs):
    print('이름 :', kwargs['name'])
    print('id :', kwargs['id'])
  
  # print_data2(name = 'hjl', id = 1234) -> 이름 : hjl id : 1234 로 출력됨
  ```

* 변수의 범위 scope

  * 지역 Local

    * 함수 내부에서만 영향을 미치는 변수

  * 전역 Global

    * 전체 스크립트에 영향을 미치는 변수

    ```python
    var = "global"
    
    def scope_var():
        var = "local"
        print(var)
    
    print(var) # global 이 출력
    # scope_var 내부에서만 사용되는 var 이 local
    
    scopre_var() # local 출력
    # 함수를 호출해야 함수 내부 var 이 출력된다
    ```

  * 전역 변수를 변경하는 방법

    * 변경 실패

    ```python
    var = "global"
    
    def scope_var(var):
        var = "local"
        print(var)
    # 처음에는 global 이 나온다
    print(var)
    # 그 다음으로 scope_var 로 var 을 바꿔주면 local 출력
    scope_var(var)
    # 다음으로 var 을 다시 출력해도 전역이기 때문에 global 출력
    print(var)
    ```

    * 변경 성공
      * 내부 함수에서 외부 변수 변경하려면 `return`, `global` 사용

    ```python
    # return
    num = 100
    
    def print_num(num):
      num = num + 1
      return num
    
    # 함수에서의 return 값을 재할당
    num = print_num(num)
    ```

    ```python
    # global
    num = 100
    
    def print_num():
        # 파라미터로 전달된 값이 없어서 안 나와야 정상
        # 하지만 global 변수, 위에 정의된 num 을 쓰게 되는 것이므로 101이 출력된다
        global num
        return num + 1
    
    print_num() # 101
    # 그러나 기존에 있는 num 의 값은 변경되지 않아서 100 으로 출력
    ```

  **하지만 global 은 지양!!**

  * 범위를 벗어나는 변수이므로 사용 지양할 것을 권장



## 객체와 클래스

### 클래스

**데이터와 기능을 묶음으로 제공하는 방법으로 객체를 만들기 위한 설계도**

```python
class 클래스이름:
    [변수명 = 데이터]
    
    [def 메서드명(self, [매개변수, ...]):
    	수행코드]
    ...
```

* 구성 요소
  * **속성 Attribute** 클래스 내부에 포함되는 변수, 데이터
  * **메서드 Method** 클래스 내부에 구현되는 함수, 기능
    * 메서드의 첫 번째 매개변수로 self 를 명시한다
    * 스페셜 메서드
      * 메서드 이름 앞 뒤로 `__` 붙어서 자동으로 호출 해주는 메서드
      * `__init__` 메서드
        * 인스턴스 (객체) 생성 시 자동 호출
        * 인스턴스 초기화
* 클래스의 이름은 대문자로 시작

```python
# 자동차 클래스 Car
class Car:
    # 속성 : 색상, 브랜드, ...
    model_name = 'G'
    color = 'R'
    
    # 기능 : 시동 on, off ...
    def turn_on(self):
        print("시동이 켜졌습니다")
    def turn_off(self):
        print("시동이 꺼졌습니다")
```

* 객체 생성

  ```python
  # 객체 생성 (인스턴스화)
  car = Car()
  
  # 메모리에 올라가서 인스턴스가 됐으므로 자동완성 가능
  car.model_name # 'G'
  car.color # 'R'
  ```

  ```python
  # 메서드 사용
  # 그러나 동작하지 않음! 내부에 parameter 가 반드시 들어가야 한다 -> self
  # 현재 def turn_on(): 으로만 작성됨
  car.turn_on() # self 로 수정하면 정상 작동 
  ```

* 스페셜 메서드

  ```python
  # 처음 생성 시 초기화해주고 싶은 것 (항상 R color 가 아니도록!)
  class Car:
      # self 는 필수
      # 현재 color 는 외부에서 들어온 매개변수로, 이 외부 변수를 내부 변수에 할당
      def __init__(self, color, model):
          self.color = color
          self.model = model
  ```

  ```python
  # 초기 생성 시 지정한 값 넣으면 할당 됨!
  bk_car = Car('bk')
  print(bk_car.color) #bk
  ```

  * 초기 값을 주면 값이 없어도 객체 생성 가능

    ```python
    # 아스타 문자 주기
    class Car:
        def __init__(self, *color):
            self.color = color
            
    # None 값으로 초기값 주기
    class Car:
        def __init__(self, color=None):
            self.color = color
    ```

    

### 객체 (인스턴스)

**물리적으로 실제 존재하는 물건 혹은 추상적인 개념**

* **객체 지향 프로그래밍 (OOP, Object-Oriented Programming)** 
* 객체로 존재하다가 실제로 운영되는 곳 (메모리) 에 올라 갔을 때 인스턴스라고 말한다

```python
객체 변수 이름 = 클래스 이름 ( [매개변수1], [매개변수2], ...)
```

* `객체변수.속성이름` , `객체변수.메서드이름` 으로 활용



