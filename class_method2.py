# 객체 지향 프로그래밍(oop) -> 코드의 재사용, 코드 중복 방지, 유지보수, 대형 프로젝트
# 규모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

class Car():
    '''
    Car class
    Author : Hwang
    Date : 2020.07.23
    '''

    # 클래스 변수(모든 인스턴스가 공유)
    car_count = 0

    def __init__(self, company, details):
        self._company = company
        self._details = details
        self.car_count = 10
        Car.car_count += 1
    def __str__(self):
        # print문으로 사용자 입장에서 출력을 원할때
        return "str : {} - {}".format(self._company,self._details)

    def __repr__(self):
        # 텍스트 뿐만 아니라 객체 정보도 표시해줌.
        return "repr : {} - {}".format(self._company, self._details)

    def __del__(self):
        Car.car_count -= 1

    def detail_info(self):
        print("Current ID : {}".format(id(self)))
        print("Car Detail Info {} {}".format(self._company,self._details.get("price")))

# self 의미 : 고유의 값(id)을 저장하기 위한 예약어
car1 = Car("Ferrari", {"color" : "white" , "horsepower" : 400, "price" : 8000})
car2 = Car("Bmw", {"color" : "black" ,"horsepower" : 270,"price" : 5000})
car3 = Car("Audi", {"color" : "red","horsepower" : 300, "price" : 6000})

# ID 확인
print(id(car1))
print(id(car2))
print(id(car3))

print(car1._company == car2._company)
# id값 기준으로 확인
print(car1 is car2)

# dir & __dict__ 확인
# 상속받는 모든 것 표시
print(dir(car1))
print(dir(car2))

print()
print()
# 속성값까지 표시해줌.
print(car1.__dict__)
print(car2.__dict__)

# Doctring
# 달아놓은 설명을 print해줌.
print(Car.__doc__)

# 실행
car1.detail_info()
Car.detail_info(car1)
car2.detail_info()
Car.detail_info(car2)
car3.detail_info()
Car.detail_info(car3)

# 에러
# Car.detail_info()

# 비교
print(car1.__class__, car2.__class__)
print(id(car1.__class__), id(car2.__class__), id(car3.__class__))
print(id(car1.__class__) == id(car2.__class__) == id(car3.__class__))

# 공유 확인
print(car1.car_count)
print(car2.car_count)
print(car1.__dict__)
print(car2.__dict__)
print(dir(car1))

# 접근
print(car1.car_count)
print(Car.car_count)

del car2
# 삭제 확인
print(car1.car_count)

# 인스턴스 네임스페이스에 없으면 상위에서 검색
# 즉, 동일한 이름으로 변수 생성 가능(인스턴스 검색 후 없으면 상위(클래스 변수, 부모 클래스 변수))
print(car1.car_count) # 10
print(Car.car_count) # 2