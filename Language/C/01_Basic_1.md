### Visual Studio IDE 설치

**프로젝트 생성**

1. `Windows Desktop Wizard` 클릭
2. 프로젝트 이름과 경로 설정
3. Solution name 을 `solution` 을 붙여서 설정
4. `Console Application` 선택 (공부 시)
5. 생성 완료

---

### 코드 실행

**ctrl + F5 (start without debugging)**

---

### C 특징

**고수준 프로그래밍 언어 (High-level Programming Language)**

**컴파일러**

* 소스 코드를 컴파일
* 소스 코드가 너무 많을 시 오브젝트 코드로 쪼개서 컴파일

**링커**

* 오브젝트 코드가 여러 개 있을 때 링크로 연결해서 실행 파일 만드는 것

* 라이브러리 코드
  * 링커가 라이브러리를 인식해서 링크해 준다
* 착수 (start-up) 코드
  * 프로그램이 시작할 때 공통으로 실행되는 것 (eg. 메모리 할당)

```c
#include <stdio.h> // standard input output 이라는 라이브러리 사용한다는 의미

int main()
{
	printf("Hello, World!");
    
    return 0;
}
```

* Build &rarr; Clean Solution 하면 `.exe`, `solution` 사라진다 
  * 파일명을 오른쪽 마우스 클릭 후 `Open Containing Folder` 클릭 

---

### Visual Studio IDE 사용법

**Solution 에 프로젝트 추가**

* Solution 오른쪽 마우스 클릭 &rarr; Add 선택, New Project 생성
  * C++ 로 생성되므로 템플릿 save 하면 좋음
  * 템플릿 만들고 싶은 기준 Project 클릭 후 메뉴에서 `Project` &rarr; `Export Template`
    * 그 후 프로젝트 추가 시 템플릿 선택 가능

* Set as Startup Project 로 해둬야 실행 시 돌아간다 

---

### 명령 프롬프트

* command 검색 후 `x86 Native Tools Command Prompt for VS 2022` 선택
* `explorer .` 
  * 현재 디렉토리 열겠다
* `cd ..`
  * 상위 디렉토리 이동
* `dir`
  * 현재 디렉토리 내 디렉토리 보기
