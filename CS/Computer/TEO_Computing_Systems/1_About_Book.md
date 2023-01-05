## 서론

### 프로그래밍 첫 수업 때 등장하는 Hello World

```tex
// jack 이라는 고수준 언어로 작성

class Main {
    function void main() {
        do Output.pringString("Hello World");
        do Output.println();
        return;
    }
}
```

**본 프로그램은 그저 텍스트 파일에 저장된 문자 덩어리일 뿐**

고수준 언어 &rarr; 컴파일 (compilation) &rarr; 저수준 언어 (기계어)

* 그러나 기계어도 미리 약속된 2진 코드로 구성된 추상화 개념
  * 따라서 기계어를 실현하기 위해서 **하드웨어 아키텍쳐 (Hardware Architecture)** 가 반드시 필요
  * 아키텍쳐 : 레지스터, 메모리 장치, ALU (Arithmetic Logic Unit) 같은 칩 들로 구성 
    * **기초 논리 게이트 (Elementary logic gate)** 집적



### 추상화

**어떤 개체의 본질을 포착해 간결한 방식으로 구별해 내는 정신적 활동을 일반적으로 의미**

&rarr; 컴퓨터 과학에서는 **'개체가 어떻게 동작 하는지'** 보다는 **'개체가 무엇을 하는지'** 로 매우 구체적으로 규정

* HW / SW 개발자는 이런 추상화 (또는 인터페이스) 를 정의하고 직접 구현하는 것
* 추상화는 층층이 쌓여 더욱 높은 단계의 기능 수행
  * **하향식 (top-down)** 방식으로도 **상향식 (bottom-up)** 방식으로도 기술 가능

**`do Output.pringString("Hello World")` 명령문**

&rarr; 문자열을 출력하라는 추상화 작업을 수행, 이 명령은 반드시 어딘가 구현돼있어야 한다



### 하드웨어 영역

**프로그램 실행 시 대상 컴퓨터 플랫폼의 기계어로 번역돼야 한다**

컴파일 과정은 복잡해서 여러 추상화 단계로 쪼개진다 

* **컴파일러**
  * 구문 분석 (syntax analysis) 와 코드 생성 (code generation) 으로 이뤄진다
    * 소스 코드의 텍스트를 분석해 의미 있는 언어 구조를 *구문 분석 트리 (parse tree)* 라 불리는 데이터 구조로 묶어내는 단계
* **가상 머신 구현 virtual machine implementation**

* **어셈블러 (assembler)**

&rarr; 그 후 하드웨어 영역에 도착

* **핵 (Hack)**
  * 단순성과 기능 사이에 균형을 잡도록 설계된 범용 컴퓨터 시스템

