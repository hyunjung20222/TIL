# 운영체제의 기초

## Evolution of OS

---

### Phase 2 ('60s ~ '90s)

#### Hardware cheap, Humans Expensive

* 그러나 현재에 비해선 고가의 HW

  * Cheap 한 것은 **Terminal**

    > 중앙 컴퓨터와 연결돼 데이터를 입출력할 수 있는 하드웨어 장치

  * `DEC` 회사에서 만든 `VT-100` 터미널이 가장 보편적

  * 실제로 프로그래머들에게 컴퓨터 1대 씩은 못줬지만, Terminal 제공

    * CPU 는 하나인데 Terminal 에는 여러 User

    * **Interactive Time Sharing Operating System 등장**  

      > CPU 의 시간을 여러 User 에게 나눠주는 것

* Time Sharing OS 가 등장하면서 개인 소유 컴퓨터라는 의식이 생김
  * Private 한 정보를 저장하기 시작
    * 개인정보 문제
      * File System 재설계 : 사용자의 소속 규정, 특정 파일의 접근 제한 등
  * 컴퓨터 시스템 평가 기준 변화
    * 사람들의 사용감이 메인 기준
      * Response Time, Private 데이터 보호 정도 등