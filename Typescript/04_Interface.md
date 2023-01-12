## 인터페이스

**상호 간에 정의한 약속 혹은 규칙을 의미하며 타입스크립트에서는 다음과 같은 범주 내 약속이 있다**

* 객체의 스펙 (속성과 속성의 타입)
* 함수의 스펙 (파라미터, 반환 타입 등)
* 배열과 객체를 접근하는 방식
* 클래스

인터페이스는 중복된 코드를 제거할 때 효율적

---

| [활용](#활용) | [옵션](#옵션) | [인덱싱](#인덱싱) | [읽기 전용](#읽기-전용) | [딕셔너리 패턴](#딕셔너리-패턴) | [타입 체킹](#타입-체킹) | [함수 타입](#함수-타입) | [클래스 타입](#클래스-타입) | [인터페이스 확장](#인터페이스-확장) | [하이브리드 타입](#하이브리드-타입) |
| ------------- | ------------- | ----------------- | ----------------------- | ------------------------------- | ----------------------- | ----------------------- | --------------------------- | ----------------------------------- | ----------------------------------- |

---

### **활용**

기존의 경우, 인자를 받을 때 속성 (age) 과 타입 (number) 을 정의할 수 있다

```tsx
let person = { name: 'Capt', age: '28' };

function logAge(obj: { age: number }) {
    console.log(obj.age); // 28
}
logAge(person); // 28
```

*인터페이스 적용 시*

```tsx
// 인터페이스 선언
interface personAge {
    age: number;
}

function logAge(obj: personAge) {
    console.log(obj.age);
}
let person = { name: 'Capt', age: '28' };
log(person); // 28
```

* 인터페이스 사용 시 항상 인터페이스의 속성 개수와 인자로 받는 객체의 속성 개수를 일치 시키지 않아도 된다
  * 인터페이스 내부 속성, 타입 조건만 만족하면 객체의 속성 개수가 더 많아도 상관 없다
  * 인터페이스에 선언된 속성 순서를 지키지 않아도 된다



### **옵션**

인터페이스에 정의돼있는 속성을 모두 사용하지 않아도 상관 없다

```tsx
interface 인터페이스_이름 {
  속성?: 타입;
}
```

* 예시

  ```tsx
  // hop 는 사용해도 되고 사용하지 않아도 되는 옵션 속성
  interface CraftBeer {
    name: string;
    hop?: number;  
  }
  
  // 그래서 myBeer 가 name 속성만 가져도 인터페이스 사용 가능
  let myBeer = {
    name: 'Saporo'
  };
  function brewBeer(beer: CraftBeer) {
    console.log(beer.name); // Saporo
  }
  brewBeer(myBeer); // Saporo
  ```

* 장점
  * 인터페이스에 정의돼있지 않은 속성을 인지 시켜 줄 수 있음
  * 만일 옵션 속성을 정의해놓지 않으면 어떤 속성이 포함돼있는지, 포함돼있지 않은지 구분 어려움



### **인덱싱**

인덱스에 형식을 지정할 수 있다

```tsx
interface StringArray {
    [index: number]: string;
}

const arr: StringArray = ['a', 'b', 'c'];
arr[0] = 10 // Error! string 에 number 할당 불가능
```



### **읽기 전용**

인터페이스로 객체를 처음 생성할 때만 값을 할당, 그 후로는 변경 불가능

```tsx
// 문자열을 읽기 전용으로 생성
interface CraftBeer {
    readonly brand: string;
}

// 배열을 읽기 전용으로 생성
let arr: ReadonlyArray<number> = [1, 2, 3]
```

* 수정 시 오류 발생

  ```tsx
  // 생성된 문자열 인터페이스 수정
  let myBeer: CraftBeer = {
      brand: 'Belgian Monk'
  };
  myBeer.brand = 'Korean Carpenter'; // Error!
  
  // 생성된 배열 인터페이스 수정
  arr.splice(0, 1) // Error!
  arr.push(4) // Error!
  ```

  

### **딕셔너리 패턴**

```tsx
interface StringRegexDictionary {
    [key: string]: RegExp; // 정규 표현식
}

const obj: StringRegexDictionary = {
    // cssFile: 'css' // Error! 정규 표현식이 와야 하는데 문자열이 온 것
    cssFile: /\.css$/
}
```

* 참고: 정규 표현식이란?

  * 정규식은 문자열에서 특정 문자 조합을 찾기 위한 패턴

  * 리터럴 / 생성자 호출로 사용 가능

    ```js
    // 리터럴 사용
    const re = /ab+c/
    
    // 생성자 호출
    const re = new RegExp('ab+c')
    ```

    https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Regular_Expressions



### **타입 체킹**

인터페이스 이용 시 속성 검사를 엄밀하게 진행한다

선언된 인터페이스 내부 속성에 객체 속성이 없다면 오탈자 체크 및 없다는 Error 가 뜬다

```tsx
interface CraftBeer {
  brand?: string;
}

function brewBeer(beer: CraftBeer) {
  // ..
}
brewBeer({ brandon: 'what' }); 
/* 
error: Object literal may only specify known properties, but 'brandon' does not exist in type 'CraftBeer'. Did you mean to write 'brand'?
*/
```

*  이를 무시하고자 할 때

  ```tsx
  let myBeer = { brandon: 'what' }';
  brewBeer(myBeer as CraftBeer);
  ```

* 인터페이스에 정의하지 않은 속성을 추가로 사용하고 싶을 때

  ```tsx
  interface CraftBeer {
    brand?: string;
    [propName: string]: any;
  }
  ```

  

### **함수 타입**

인터페이스는 함수 정의 시에도 사용 가능

&rarr; 함수의 인자의 타입과 반환 값의 타입을 지정 (함수의 스펙 (구조) 에 인터페이스 활용하는 것)

```tsx
interface SumFunction {
  (a: number, b: number): number;
}

let sum: SumFunction;
sum = function(a: number, b: number): number {
    return a + b;
}
```



### **클래스 타입**

클래스가 일정 조건을 만족하도록 타입 규칙을 정할 수 있다

```tsx
interface CraftBeer {
  beerName: string;
  nameBeer(beer: string): void;
}

// 인터페이스 implenets 로 클래스에 이식
class myBeer implements CraftBeer {
  beerName: string = 'Baby Guinness';
  nameBeer(b: string) {
    this.beerName = b;
  }
  constructor() {}
}
```



### **인터페이스 확장**

클래스와 마찬가지로 인터페이스도 인터페이스 간 확장 가능

```tsx
interface Person {
  name: string;
  age: number;
}

// 인터페이스 extends 로 확장
interface Developer extends Person {
  language: string;
}
let fe = {} as Developer;
fe.name = 'josh';
fe.language = 'TypeScript';
```



### **하이브리드 타입**

JS 처럼 인터페이스도 여러 가지 타입을 조합해 만들 수 있다

* 함수 타입이면서 객체 타입을 정의할 수 있는 인터페이스

  ```tsx
  interface CraftBeer {
    (beer: string): string;
    brand: string;
    brew(): void;
  }
  
  function myBeer(): CraftBeer {
    let my = (function(beer: string) {}) as CraftBeer;
    my.brand = 'Beer Kitchen';
    my.brew = function() {};
    return my;
  }
  
  let brewedBeer = myBeer();
  brewedBeer('My First Beer');
  brewedBeer.brand = 'Pangyo Craft';
  brewedBeer.brew();
  ```

  