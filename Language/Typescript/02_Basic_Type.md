## 기본 변수 타입

| [문자열](#문자열) | [숫자](#숫자) | [배열](#배열) | [튜플](#튜플) | [Enum](#enum) | [객체](#객체) | [Boolean](#boolean) | [Any](#any) | [Void](#void) | [Never](#never) | Null | Undefined |
| ----------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------------- | ----------- | ------------- | --------------- | ---- | --------- |

---

### **문자열**

```js
// JS 코드
const str = 'hello';
```

```tsx
// TS 코드
const str: string = 'hello';
```

* `:` 를 이용해 JS 코드에 타입을 정의하는 방식을 `타입 표기 (Type Annotation)` 이라고 한다



### **숫자**

```tsx
// TS 숫자
const num: number = 10;
```



### **배열**

```tsx
// TS 배열 (제네릭 사용)
const arr: Array<number> = [1, 2, 3]
const heros: Array<string> = ['Thor', 'Hulk']

// 배열 앞에 타입 써도 가능
const items: number[] = [1, 2, 3]
```

* 제네릭과 타입[] 의 차이점

  https://velog.io/@k2hyun4/typescript-ArrayType-vs-Type

  결론 : 없다! &rarr; 적절하게 맞춰 사용하면 되겠다

### **튜플**

```tsx
// TS 튜플 
// 배열의 길이가 고정되고 각 요소의 타입이 지정돼있는 배열 형식
const address: [string, number] = ['gangnam', 100];

// 정의하지 않은 타입, 인덱스로 접근할 경우 오류
```



### **Enum**

특정 값 (상수) 들의 집합을 의미

```tsx
enum Avengers {Capt, IronMan, Thor}
const hero: Avengers = Avengers.Capt;

// 이넘은 인덱스 번호로도 접근 가능
const hero: Avengers = Avengers[0];

// 이넘의 인덱스를 사용자 편의로 변경해 사용 가능
enum Avengers {Capt = 2, Ironman, Thor}
```



### **객체**

```tsx
// TS 객체
const obj: object = {}
const person: object = {
    name: 'capt',
    age: 100
}

// property name 과 age 를 명시해줘야 한다
const person: {name: string, age: number} = {
    name: 'thor',
    age: 1000
}
```



### **Boolean**

```tsx
// TS 진위값
const show: boolean = true;
```



### Any

기존 자바스크립트로 구현된 웹 서비스 코드에 타입스크립트 점진적 활용에 좋은 타입

모든 타입에 대해 허용한다는 의미

```tsx
// TS Any
const str: any = 'hi';
const arr: any = ['a', 2, true];
```



### Void

변수에는 `undefined` 와 `null` 만 할당하고 함수에는 반환 값을 설정할 수 없는 타입

```tsx
const unuseful: void = undefined;
function notuse(): void {
    console.log('sth')
}
```



### Never

함수의 끝에 절대 도달하지 않는다는 의미

```tsx
// 선언된 함수는 절대 함수의 끝까지 실행되지 않는다는 의미
function neverEnd(): never {
    while (true) {
        
    }
}
```