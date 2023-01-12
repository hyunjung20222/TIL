**목차**

1. [자동 타입 변환](#자동-타입-변환)
2. [강제 타입 변환](#강제-타입-변환)
3. [출력](#출력)
4. [키보드 입력 데이터를 변수에 저장](#키보드-입력-데이터를-변수에-저장)

---

### 자동 타입 변환

**값의 허용 범위가 작은 타입이 허용 범위가 큰 타입으로 대입될 때 발생**

`byte < short, char < int < long < float < double`

```java
// int 타입이 byte 타입보다 허용 범위가 크기 때문에 다음 코드 성립

byte byteValue = 10;
int intValue = byteValue;
```

* 예외
  * 허용 범위가 작은 `byte` 지만 `char` 에 자동변환 되지 않는다
    * `char` 은 음수를 포함하고 있지 않기 때문이다

---

### 강제 타입 변환

**큰 허용 범위를 작은 단위로 쪼개서 작은 허용 범위에 저장하는 것**

`작은 허용 범위 타입 = (작은 허용 범위 타입) 큰 허용 범위 타입`

```java
int intValue = 10;
byte byteValue = (byte) intValue;
```

* 작은 허용 범위 내의 값만 원래 값을 보존할 수 있다

#### 연산식에서 자동 타입 변환

* 정수 리터럴이 아니라 변수가 피연산자로 사용되면 실행 시 연산을 수행한다
  * `int` 타입보다 작은 `byte`, `short` 타입의 변수는 `int` 타입으로 자동 타입 변환 돼 연산 수행

```java
byte x = 10;
byte y = 20;

// 이 경우, int 변환돼서 연산 실행되므로 컴파일 에러
byte result = x + y;

// 이 경우, int 변환되므로 컴파일 성공
int result = x + y;
```

* 작은 허용 범위에서 큰 허용 범위로 자동 타입 변환
  * eg. `int` &rarr; `long`

#### 문자열을 기본 타입으로 변환

| 변환 타입                 | 사용 예                                                      |
| ------------------------- | ------------------------------------------------------------ |
| `String` &rarr; `byte`    | String str = "10";<br />byte value = Byte.parseByte(str);    |
| `String` &rarr; `short`   | String str = "200";<br />shortvalue = Short.parseShort(str); |
| `String` &rarr; `int`     | String str = "300000";<br />int value = Integer.parseInt(str); |
| `String` &rarr; `long`    | String str = "40000000000";<br />byte long = Long.parseLong(str); |
| `String` &rarr; `float`   | String str = "12.345";<br />float value = Float.parseFloat(str); |
| `String` &rarr; `double`  | String str = "12.345";<br />double value = Double.parseDouble(str); |
| `String` &rarr; `boolean` | String str = "true";<br />boolean value = Byte.parseBoolean(str); |

**기본 타입의 값을 문자열로 변경하는 경우**

```java
String str = String.valueOf(기본타입)
```

---

#### 출력

```java
System.out.print--
```

| 메소드                                | 의미                                    |
| ------------------------------------- | --------------------------------------- |
| `println(내용);`                      | 괄호 안의 내용을 출력 후 행 바꾸기      |
| `print(내용);`                        | 괄호 안의 내용을 출력 후 행 바꾸지 않기 |
| `printf("형식문자열", 값1, 값2 ... )` | 형식 문자열에 맞춰 뒤의 값을 출력       |

**형식 문자열**

* 정수 : `%d`
* 실수 : `%f`
* 문자열 `%s`

---

### 키보드 입력 데이터를 변수에 저장

**Scanner 사용**

```java
Scanner scanner = new Scanner(System.in);
    
// 키보드로 입력된 내용을 문자열로 읽고 좌측 String 변수에 저장 가능
String inputData = scanner.nextLine();
```

