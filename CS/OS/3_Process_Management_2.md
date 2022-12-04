**목차**

1. [fork () 시스템 콜](#fork-()-시스템-콜)
2. [exec () 시스템 콜](#exec-()-시스템-콜)
3. [wait () 시스템 콜](#wait-()-시스템-콜)
4. [exit () 시스템 콜](#exit-()-시스템-콜)
5. [프로세스 간 협력](#프로세스-간-협력)

---

### fork () 시스템 콜

**fork () 를 하게 되면 fork 이후의 코드부터 자식이 실행!**

* fork () 해서 무한 fork 되지 않는다
* fork () 의 결과값이 다르기 때문에 부모 / 자식 구분이 가능하다

```c
int main()
{
int pid;
pid = fork()
if (pid == 0)
	printf("Children")
else if (pid > 0)
	printf("parent")
}
```

---

### exec () 시스템 콜

**fork () 와 다르게 fork 후에 새로운 프로그램으로 덮어쓰이는 것**

* 반드시 fork 해야 새로운 시스템으로 씌워지는 것은 아니다
* exec 이후 코드는 실행할 수 없다 (부모 / 자식 나누지 않는 한)

```C
int main()
{
int pid;
pid = fork()
if (pid == 0)
{
    printf("Children")
        execlp("/bin/date", "/bin/date", (char *) 0)
        /*date 라는 프로그램으로 덮어씌워지는 것*/
}
else if (pid > 0)
	printf("parent")
}
```

---

### wait () 시스템 콜

**프로세스 A 가 wait() 시스템 콜을 호출할 때**

* 커널은 child 가 종료될 때까지 프로세스 A 를 sleep 시킨다 (block 상태)
* Child Process 가 종료되면 커널은 프로세스 A 를 깨운다 (ready 상태)

---

### exit () 시스템 콜

**프로세스의 종료**

* 자발적 종료
  * 마지막 statement 수행 후 exit () 시스템 콜을 통해 
  * 프로그램에 명시적으로 적어주지 않아도 main 함수가 리턴되는 위치에 컴파일러가 넣어준다
* 비자발적 종료
  * 부모 프로세스가 자식 프로세스 강제 종료
    * 자식 프로세스가 한계치를 넘어서는 자원 요청
    * 자식에게 할당된 태스크가 필요치 않음
  * 키보드로 kill, break 등을 친 경우
  * 부모가 종료하는 경우 부모 프로세스가 종료하기 전에 자식들이 먼저 종료

---

### 프로세스 간 협력

**독립적 프로세스**

* 프로세스는 각자의 주소 공간을 가지고 수행
* 원칙적으로 하나의 프로세스는 다른 프로세스의 수행에 영향을 미치지 못한다

**협력 프로세스**

* 프로세스 협력 메커니즘을 통해 하나의 프로세스가 다른 프로세스의 수행에 영향을 미칠 수 있다
* **프로세스 간 협력 메커니즘 (IPC : Interprocess Communication)**
  * 메시지를 전달하는 방법
    * **message passing** 
      * 커널을 통해 메시지 전달
      * 프로세스 사이에 공유 변수 (shared variable) 를 일체 사용하지 않고 통신
      * **Direct Communication**
        * 통신 프로세스 이름 명시적 표시
      * **Indirect Communication**
        * mailbox (또는 port) 를 통해 메시지 간접 전달
  * 주소 공간을 공유하는 방법
    * **shared memory**
      * 서로 다른 프로세스 간에도 일부 주소 공간을 공유하게 하는 메커니즘
    * **thread**
      * thread는 사실상 하나의 프로세스이므로 협력으로 보기는 어렵다
      * 그러나 동일한 process 를 구성하는 thread 간에는 주소 공간을 공유하므로 협력이 가능하다