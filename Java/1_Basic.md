## 기초

### 소스 작성 / 실행

```tex
tmep
|-- src  소스 파일이 저장되는 디렉토리
|    |-- ch01  패키지 디렉토리
|          |-- sec06 패키지 디렉토리
|                 |-- Hello.java 소스 파일
|-- bin 바이트 코드 파일이 저장되는 디렉토리
```



**소스 작성**

```java
// 바이트 코드 파일이 위치할 패키지 선언
package ch01.sec06

/*
Hello 클래스 선언 후 main() 메소드 선언
그 후 콘솔에 출력하는 코드 작성
*/

public class Hello {
    public static void main(String[] args) {
        System.out.println("Hello, java")
    }
}
```

* `package ch01.sec09`
  * 패키지 선언
  * 소스 파일이 `src/ch01/sec09` 에 있다는 것을 의미
  * 컴파일 후 생성되는 바이트 코드 파일도 `bin/ch01/sec09` 패키지에 생성된다
* `public class Hello`
  * 클래스 선언
  * `Hello` 는 클래스명
    * 숫자로 시작할 수 없고 공백을 포함해서는 안된다
    * 소스 파일명과 대소문자가 완벽히 일치해야 한다
  * 그 후 중괄호를 클래스 블록이라 하며 클래스의 정의 내용이 포함된다
* `public static void main(Stirng[] args)`
  * 메소드
  * 중괄호 이후를 메소드 블록
    * 바이트 코드 파일을 실행 시 main() 메소드 블록이 실행 (실행 진입점)
* 실행문 끝에는 반드시 **세미콜론** `;` 을 붙여야 한다



**컴파일**

|            | 코드 / 설명                                                  |
| ---------- | ------------------------------------------------------------ |
| **컴파일** | ``javac -d [바이트 코드 파일 저장 위치] [소스경로/*.java]`<br />`javac -d bin src/ch01/sec06/Hello.java` |
| 결과       | `temp/bin` 디렉토리에 바이트 코드 파일 (`ch01/sec06/Hello.class`) 이 생성 |
| **실행**   | `java -cp [바이트 코드 파일 위치] [패키지.. 클래스명]`<br />`java -cp bin ch01.sec06.Hello` |
| 결과       | 콘솔에 `Hello, java`가 출력된다                              |

