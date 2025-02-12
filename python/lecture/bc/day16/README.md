# OOP (Object Oriented Programming)

절차 지향 프로그래밍에서 모든 시그니처들이 얽히고 설켜서 코드의 유지보수가 어려워지는 문제점을 해결하기 위해 등장한 개념이 객체 지향 프로그래밍이다. 
객체 지향 프로그래밍은 데이터와 데이터를 처리하는 함수를 하나의 단위로 묶어서 관리하는 프로그래밍 방법이다.

회를 사먹는 사람이 생선을 해체하는 방법을 아는 것이 아닌 본인의 전문 분야에 집중하여 돈을 벌어 회를 사먹는 것이 더 효율적인 것처럼 
자본주의 사회와 비슷한 면이 있다.

## 예시

Waiter(웨이터)를 만들어보자.
has:
- name
- age
- salary
does:
- greet
- serve
- clean

has를 멤버 변수(attribute)라고 하고 does를 멤버 함수(method)라고 한다.
```python
class Waiter: # 클래스의 이름은 파스칼 표기법을 따른다. 
    def __init__(self, name, age, salary): # 생성자
        self.name = name
        self.age = age
        self.salary = salary

    def greet(self):
        print(f"Hello, my name is {self.name}")

    def serve(self):
        print(f"{self.name} is serving")

    def clean(self):
        print(f"{self.name} is cleaning")
