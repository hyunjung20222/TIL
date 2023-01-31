**목차**

1. [DDL (Data Definition Language)](#ddl-(data-definition-language))

   * [테이블](#테이블)

   * [데이터](#데이터)

2. [DML (Data Manipulation Language)](#dml-(data-manipulation-language))

---

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

---

## DML (Data Manipulation Language)

**데이터 조작 언어로 이미 존재하는 table 에 데이터 저장, 수정, 삭제, 검색 등 수행하는 것**

**commit** 

* 영구 저장

**rollback**

* 복원 문장 필수

**Insert**

* 테이블에 삽입 

  ```sql
  # column 기술하지 않고 삽입
  INSERT INTO people VALUES('hj', 30);
  
  # column 기술하고 삽입
  INSERT INTO people(age, name) VALUES(30, 'hj');
  # 컬럼 순서 상관없이 지정한 대로 삽입하면 되지만, 일반적으로 순서를 지키도록 함
  ```

* 다중 table 에 데이터 insert 도 가능하지만, oracle 에서 사용하는 문법

  * MySQL 에서는 여러 번 같은 동작을 하면 된다

  * 너무 많은 경우 `,` 으로 한 번에 여러 개 데이터 넣을 수 있다

    ```sql
    # Bulk Insert
    INSERT INTO people VALUES('hj', 30), ('hi', 20), ('hu', 10);
    ```



**update**

* 테이블의 모든 행 변경

  ```sql
  UPDATE emp01
  SET deptno = 30;
  ```

  * 하지만 여기서 deptno 는 고유한 값이 아니기 때문에 변경안됨

    * 변경하려면 설정을 바꿔야 한다

  * 변경 후 rollback 

    ```sql
    ROLLBACK
    # 하지만 적용 안됨.. 이미 commit 돼서 영구 저장 돼버림
    ```

    * ***auto commit 주의***

      ```sql
      # 1 로 설정돼있는 것을 0 으로 바꿔줘야 비활성화
      SELECT @@autocommit;
      ```

* 참고

  ```sql
  # 서브 쿼리로 보다 편리하게 다중 테이블 사용 가능
  UPDATE emp01
  SET sal = sal + 1000
  WHERE deptno = (
  				SELECT deptno
  				FROM dept
  				WHERE loc = 'DALLAS');
  ```



**Delete**

```sql
DELETE FROM emp01;
# TRUNCATE 와 비슷하나 Delete 는 DML 이기 때문에 rollback 으로 데이터를 복구할 수 있다
# TRUNCATE 는 DDL 이기 때문에 복구 불가능
```

* 특정 row 만 삭제

  ```sql
  DELETE FROM emp01
  WHERE deptno = 10;
  ```

