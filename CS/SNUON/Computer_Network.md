# 컴퓨터 네트워크

## 개념

#### 컴퓨터의 통신 (Communication)

* Communication is exchange of info between users at a distance 
  * 반드시 사람일 필요는 없으며 반드시 두 사람일 필요도 없다
    * 컴퓨터, 스마트폰, 서버 간 통신이거나 1 : N 관계

#### 네트워크 (Network)

* A system consists of devices (often referred to as nodes) and links for transportation of entities
  * eg. roads, railroads, water
  * 노드와 링크로 구성된 시스템이 네트워크

* **Two Types of communication Networks (통신망)**
  * Voice : 음성신호를 움직이는 망 (전화망)
    * Computer networks : 디지털 정보 (디지털화 된) 를 움직이는 망
      * LTE 가 되며 음성 신호를 디지털화, 현재 스마트폰 통화는 전화망 X
* Connectivity
  * Impossible to connect (large) number of users (nodes) directly
  * Share resources (links)
    * Network is a mechanixm to make the connectivity easy by sharing resources
  * Sharing mechanisms
    * Multiplexing
    * Access control

#### 통신 타입

* **Simplex**
  * Mainframe ------------------> Monitor
* **Half-duplex**
  * Station <----------------------> Station
    * 양방향 전송이 가능하나, 한 쪽의 전송이 끝나야 다른 방향 전송 가능
* **Full-duplex**
  * Station <-----------------------> Station
    * 동시에 양방향 전송 가능

#### 링크 타입

* **Point-toPoint**
  * Station ------- Link -------- Station
    * 양 쪽의  스테이션만 Link 를 직접적으로 사용 가능
    * **Multiplexing**
* **Multipoint**
  * Mainframe -------- Link ------ Station --- Station --- Station
    * 여러 스테이션이 한 Link 를 공유
    * **Access Control**
      * 한 스테이션만 전송 가능
      * 동시에 여러 스테이션 전송 불가
    * **Broadcast Link** 
      * 한 스테이션이 공유했을 때 Link 와 연결된 모든 스테이션이 정보 받기 가능

####  Architecture (구조)

* Divide & Conquer

  * To solve large & complex problem, first, partition the problem into small pieces
  * Solve each partial problem
  * Combine sub-solutions into a whole solution
    * 작은 조각으로 나눠서 차근히 해결

* **Architecture**

  * A set of sub-functions that comprise a larger function
    * 큰 기능을 수행하기 위한 작은 기능들의 집합

* Abstraction

  * Shield internal implementationn details and show only interfaces
    * 기능들이 자기 일을 하기 위해서 Procedure 진행
      * 그 과정의 세세한 정보를 보여주지 않고 추상화
      * Parameter, Variable 선언 / 정의 등

* **Layered Architecture (계층 구조)**

  * Keep the interaction simple

  > Layer N
  >
  > 
  >
  > Layer n + 1
  >
  > Layer n
  >
  > Layer n - 1
  > 
  >
  > Layer 1

  * 1에 가까울 수록 Raw, N 에 가까울수록 (높을수록) Abstract
  * Layer n uses service probided by layer n-1, adds its own functions and provide  more abstract service to layer n+1
  * 7 계층
    * Layer 1 에서는 0, 1 정보를 Electric Magnetic Signal 로 변환
    * 정보 압축, 코딩까지 Layer 1 에서 수행
    * Layer N 에서는 사람 (사용자) 이 바로 쓸 수 있는 프로토콜
      * 주로 Application 이라 부른다