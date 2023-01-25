**목차**

1. [테이블](#테이블)
2. [데이터](#데이터)

## DDL (Data Definition Language)

**데이터가 들어갈 수 있는 테이블을 만드는 문법**

* CRUD 는 데이터가 있어야 가능하기 때문에 DDL 이라 하지 않는다

**규칙**

* common
  * 소문자 사용하며 축약, 약어를 사용하지 않는다 (약어를 사용한다면 소문자)
  * 능동태 사용
* 테이블
  * 단수형이며 snake case 로 작성한다
* 컬럼
  * `테이블 이름_id` 로 소문자며 snake case 로 작성한다
  * `_flag`, `_date`



### 테이블 

**삭제**

```sql
DROP TABLE test;
```

**생성**

```sql
CREATE TABLE people(
name VARCHAR(20),
age INT(3)
);
# INT(3) 은 3 자리수까지 제한하는 것
```

* 서브 쿼리 활용해서 테이블 생성

  ```sql
  # emp 테이블로부터 데이터를 가져와 emp01 을 만드는 것
  CREATE TABLE emp01
  AS SELECT * FROM emp;
  ```

  * 테이블 구조만 복제

    ```sql
    CREATE TABLE emp01
    AS SELECT * FROM emp
    WHERE 1=0;
    # 거짓 조건을 줘서 데이터는 제외하고 구조만 복제할 수 있다
    ```

  * 특정 컬럼만 참조해서 복제

    ```sql
    CREATE TABLE emp02
    AS SELECT empno FROM emp;
    # empno 컬럼만 들고오는 것
    ```

---

### 데이터

**컬럼 추가**

```sql
ALTER TABLE emp01
ADD COLUMN phone varchar(13);
```

**컬럼 삭제**

```sql
ALTER TABLE emp01
DROP COLUMN phone;
```

* 테이블 데이터만 삭제

  ```sql
  TRUNCATE TABLE emp03;
  ```

**컬럼 타입 (사이즈) 변경**

* 데이터가 존재하지 않을 때

  ```sql
  # modify 사용
  ALTER TABLE emp01
  MODIFY phone VARCHAR(15);
  
  # change 사용
  ALTER TABLE emp01
  CHANGE COLUMN phone phone VARCHAR(13);
  # CHANGE COLUMN 바꾸고자 하는 현재 컬럼명 바꾸고자 하는 미래 컬럼명 타입 지정
  ```

* 데이터가 존재할 때는 **더 큰 사이즈의 컬럼**으로만 변경 가능하다

