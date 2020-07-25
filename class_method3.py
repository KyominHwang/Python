# 객체 지향 프로그래밍(oop) -> 코드의 재사용, 코드 중복 방지, 유지보수, 대형 프로젝트
# 규모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

class Car():
    '''
    Car class
    Author : Hwang
    Date : 2020.07.24
    Description : Class, Static, Instance Method
    '''

    # 클래스 변수(모든 인스턴스가 공유)
    price_per_raise = 1.0

    def __init__(self, company, details):
        self._company = company
        self._details = details

    def __str__(self):
        # print문으로 사용자 입장에서 출력을 원할때
        return "str : {} - {}".format(self._company,self._details)

    def __repr__(self):
        # 텍스트 뿐만 아니라 객체 정보도 표시해줌.
        return "repr : {} - {}".format(self._company, self._details)
    # Instance Method
    # self : 객체의 고유한 속성 값을 사용
    def detail_info(self):
        print("Current ID : {}".format(id(self)))
        print("Car Detail Info {} {}".format(self._company,self._details.get("price")))

    # Instance Method
    def get_price(self):
        return "Before Car Price -> company : {}, price : {}".format(self._company, self._details["price"])

    # Instance Method
    def get_price_calc(self):
        return "After Car Price -> company : {}, price : {}".format(self._company, Car.price_per_raise * self._details["price"])

    # Class Method
    @classmethod
    def raise_price(cls, per):
        if per <= 1:
            print("Pleas Enter 1 Or More")
            return
        cls.price_per_raise = per
        print("Succeed! price increased.")

    # Static Method
    @staticmethod
    def is_bmw(inst):
        if inst._company == "Bmw":
            return f"Ok! This car is {inst._company}"
        return "Sorry. This car is not Bmw!"

# self 의미 : 고유의 값(id)을 저장하기 위한 예약어
car1 = Car("Ferrari", {"color" : "white" , "horsepower" : 400, "price" : 8000})
car2 = Car("Bmw", {"color" : "black" ,"horsepower" : 270,"price" : 5000})

# 전체 정보
car1.detail_info()

# 가격 정보(직접 접근)
print(car1._details.get("price"))
print(car2._details["price"])

# 가격 정보(인상 전)
print(car1.get_price())
print(car2.get_price())

#가격 인상(클래스 메소드 미사용)
Car.price_per_raise = 1.4

# 가격 정보(인상 후)
print(car1.get_price_calc())
print(car2.get_price_calc())

#가격 인상(클래스 메소드 사용)
Car.raise_price(1.6)

# 가격 정보(인상 후)
print(car1.get_price_calc())
print(car2.get_price_calc())

# 인스턴스로 호출(static method)
print(car1.is_bmw(car1))
print(car2.is_bmw(car2))

# 클래스로 호출(static method)
print(Car.is_bmw(car1))
print(Car.is_bmw(car2))