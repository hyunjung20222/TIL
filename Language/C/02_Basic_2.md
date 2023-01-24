# C 언어 개괄

![문장](./assets/C_statement.png)

```c
#include <stdio.h>

// main 이라는 함수
// 정수형 숫자 하나를 받고 싶어한다
int main()
// main 이라는 함수의 body 
{
	// 수행하고 싶은 내용들 작성 

  return 0; // 정수형 숫자 하나, 함수가 끝났다는 신호로 0 사용
}
```



### 자료형

| 자료형 | 설명 |
| ------ | ---- |
| int    |      |
| short  |      |
| char   |      |
| double |      |
|        |      |



### 변수 선언법

숫자를 앞에 작성할 수 없다

`_` 사용 가능

대문자와 소문자 구분

```c
#include <stdio.h>

int main()
{
	int x; // 변수 선언 declaration
	int y; // 같은 자료형일 때 int x, y, z; 로 한 줄로 선언 가능
	int z;

	x = 1; // 값 할당 assignment 
	y = 2;

	z = x + y; // 3

	return 0;
}
```



### printf

**escape sequence** `\`

**print`f` = print formatted**

```c
int main()
{
    int x, y, z;
    
    x = 1;
    y = 2;
    
    z = x + y;
    
    printf("The answer is %i", z); // %i 자리에 z 값이 대입돼서 출력된다 (i: integer, d: decimal)
    printf("%i + %i = %i", x, y, z); // 1 + 2 = 3
    
    return 0;
}
```



### 함수

```c
#include <stdio.h>

void say_hello(void) // function definition
{
	printf("Hello, World!\n");
}


// 함수 사용 시 호출 전 선언이 돼있어야 한다
// 위에 선언하거나 void say_hello(void); 라는 프로토타입만 위에 작성해도 된다 (function declaration)
int main()
{
	say_hello();

	return 0;
}
```



