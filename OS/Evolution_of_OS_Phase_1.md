# 운영체제의 기초

## Evolution of OS

**과거부터 현재까지 Operating System 이 진화한 과정**

> OS 는 Hardware 의 발전을 Support 하기 위해 같이 진화했다
>
> 하지만 OS 의 발전으로 HW 도 진화

---

### Phase 1 (early '50s ~ '60s)

#### Hardware expensive, humans cheap

* CPU utilization 최대화 목적

* 인건비에 대한 투자는 고려 대상 X

* **Operator** 의 역할

  > 1. 사용자로부터 카드 덱을 수령
  >
  > 2. 카드 덱을 컴퓨터 시스템에 로딩하고 수행
  >
  > 3. 수행 결과를 프린터로 출력
  >
  > 4. 출력된 결과물을 사용자에게 전달
  >
  >    > Human Operator 가 수행

* **Human Operator** 의 느린 Job-to-Job 전환 속도로 인한 컴퓨터 시스템의 비효율성 해결 필요

  * #### Batch Monitor 개발

    * **IBM 1401** 

      > 1. 사용자로부터 카드 덱을 수령
      >
      > 2. 1401 이 받아서 Tape 에 저장 (여러 개의 Job 을 묶어서 저장)
      >
      > 3. 한 번에 한 Job 씩 순차 처리, 결과는 Tape 에 저장
      >
      > 4. Tape 의 Output 이 프린트, 사용자에게 전달
      >
      >    > 느린 전환 속도를 해결

    * **I/O Channel**

      > CPU 를 대신해서 I/O operation 관장
      >
      > I/O operation 시작과 끝만 CPU 가 관장
      >
      > > Interrupt 메커니즘 지원하는 Batch Monitor 최초 등장
      > >
      > > 최초의 OS 에서 CPU utilization을 낮추는 요인과 이를 극복하기 위한 하드웨어 및 OS 진화

    * #### 동기적 I/O (sync)

      * I/O 의 수행이 종료돼야만 다음 연산으로 수행할 수 있는 것
      * 대부분의 Input Operation (종속)
      * Interrupt 메커니즘의 효율성 (Utilization) 을 가질 수 없음

    * #### 비동기적 I/O (async)

      * CPU 가 I/O 수행해도 종료 때까지 기다리지 않고 바로 수행할 수 있는 것
        * 대부분의 Output Operation (비종속)

  * #### Multiprogrammed Batch Monitor

    * 한 개 이상의 **Active Job** 을 수행시키는 것

      * Active Job : 수행을 시작했지만 아직 종료되지 않은 상태의 프로그램

    * **Degree of Multiprogramming**

      * 현재 메인 메모리에 존재하고 있는 Acitve Job 의 갯수

    * #### 문제점

      * **Memory Protection**

        * C 에서 가장 어려운 게 Point Error

        * 당시에도 기계어 프로그래밍, Point Error 문제 有

        * 어떤 Job 의 주소 사용 버그로 인해 다른 Job 이나 OS 의 영역을 침범함으로써 문제를 일으키는 현상을 방지해야 할 필요성 대두

          * 메모리를 잘 보호해야 한다

          * **해결책**

            * Job 이 사용하는 메인 메모리의 시작 주소(Base Register 에 저장) 와 Job 이 사용하는 메모리의 크기 (Bound Register 에 저장) 를 사용해 현재 접근하려는 주소 없이 **Base Register ~ Base + Bound Register** 사이에 있는지 확인

              > 논리 주소 (Logical Address) : 프로그램에 의해 CPU가 바로 생성하는 주소
              >
              > 물리 주소 (Physical Address) : 일련의 변환을 거친 최종 메인 메모리 주소
              >
              > > **MMU (Memory  Management Unit)** 
              > >
              > > 논리 주소를 물리 주소로 변환하고, Memory Protection 을 Check 해주는 부분
              >
              > **MMU** 구현
              >
              > > SW 로 구현될 경우 주소 변환을 위해 다시 주소 변환이 필요해지는 성능 저하 문제 발생
              > >
              > > MMU 를 구현하기 위해 Instructions 로 구성되므로 주소 변환의 과정이 필요, 재귀적인 호출 문제 발생 
              > >
              > > 즉, **HW 로 구현해야 한다** 
              >
              > > **Is MMU transparent to OS?**
              > >
              > > No! 
              > >
              > > > Job 이 수행되다가 다른 Job 넘어갈 때 새로운 Job 의 Base/Bound Register 에 값을 Set 해줘야하는 문제
              > >
              > > **MMU 는 OS 의 고유한 권한으로 수행돼야 한다**
              > >
              > > > Privileged Instructions

      * **Memory Relocation**

        * Simple Batch Monitor 는 User Job 이 메인 메모리 특정 영역에 load 돼서 수행
        * Multi 가 되면서 하나의 Job 제외하고는 임의의 메모리 위치에서 수행
          * 기계어 프로그램일 때 어디서 시작되는지 알 수 없음
          * 즉, **Job 이 메인 메모리의 어느 위치에 load 되는지 알 수 없기 때문에 임의의 주소에서도 문제없이 수행돼야 함**
          * **해결책**
            * **Base Register** : 프로그램이 load 된 시작 주소를 담고 있는 주소
              * 0번지 부터 수행이 된다는 가정 하에 프로그래밍

      * **Concurrent Programming**

        * 여러 Job 이 동시 수행되면 공유 자원이나 공유 데이터에 동시에 접근함으로서 생기는 문제 해결 필요성 대두

