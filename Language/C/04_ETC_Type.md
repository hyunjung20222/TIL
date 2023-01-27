**목차**

1. [문자형](#문자형)
1. [Boolean 형](#boolean-형)
1. [복소수형](#복소수형)

---

## 문자형

**ASCII**

문자와 숫자를 1 : 1로 대응 시킨 것

```c
#include <stdio.h>

int main()
{
	char c = 'A';
	char d = 65;
	// 문자 출력과 숫자로 출력해주는 것
	printf("%c %hhd\n", c, c);
	printf("%c %hhd\n", d, d);
    // 아스키 코드에서는 문자와 숫자 연산 가능, B 가 출력된다
    printf("%c \n", c + 1);

	return 0;
}
```

* `\a` 는 경고음을 발생 시키는 이스케이프 문자, 아스키 코드와 대응하는 `\07` 도 같은 역할

  ```c
  #include <stdio.h>
  
  int main()
  {
      // 경고음 발생하며, \a 로 해도 경고음 발생한다
  	char b = '\07';
  	printf("%c", b);
  
  	return 0;
  }
  ```

---

## Boolean 형

```c
#include <stdio.h>
#include <stdbool.h>

int main()
{
	_Bool b1;
	b1 = 0; // false
	b1 = 1; // true
	
    // 1 출력
	printf("%d\n", b1);

	// include <stdbool.h> 쓸 경우 가능
	bool b2, b3;
	b2 = true;
	b3 = false;
    
    // 1 0 출력 된다
	printf("%d %d\n", b2, b3);

	return 0;
}
```

---

## 복소수형

```c
#include <complex.h>

int main()
{
    double _Complex z = 1 + 2*I; // 실수부와 허수부
   
    z = 1 / z;    
    printf("1 / (1.0 + 2.0i) = %.1f+.1fi\n", creal(z), cimag(z));
    return 0;
}
```

