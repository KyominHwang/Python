# 객체 지향 프로그래밍(oop) -> 코드의 재사용, 코드 중복 방지, 유지보수, 대형 프로젝트
# 규모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

# 일반적인 코딩
# 차량1
car_company_1 = "Ferrari"
car_detail_1 = [
    {"color" : "white"},
    {"horsepower" : 400},
    {"price" : 8000}
]

# 차량2
car_company_2 = "Bmw"
car_detail_2 = [
    {"color" : "black"},
    {"horsepower" : 270},
    {"price" : 5000}
]

# 차량3
car_company_3 = "Audi"
car_detail_3 = [
    {"color" : "red"},
    {"horsepower" : 300},
    {"price" : 6000}
]

# 리스트 구조
# 관리하기가 불편함.
# 인덱스 접근 시 실수 가능성, 삭제 불편
car_company_list = ["Ferrari","Bmw","Audi"]
car_detail_list = [
    {"color" : "white" , "horsepower" : 400, "price" : 8000},
    {"color" : "black" ,"horsepower" : 270,"price" : 5000},
    {"color" : "red","horsepower" : 300, "price" : 6000}
]

del car_company_list[1]
del car_detail_list[1]

print(car_company_list)
print(car_detail_list)

# 딕셔너리 구조
# 코드 반복 지속, 중첩 문제(키), 키 조회 예외 처리 등
car_dicts = [
    {"car_company" : "Ferrari", "car_detail" : {"color" : "white" , "horsepower" : 400, "price" : 8000}},
    {"car_company" : "Bmw", "car_detail" : {"color" : "black" ,"horsepower" : 270,"price" : 5000}},
    {"car_company" : "Audi", "car_detail" : {"color" : "red","horsepower" : 300, "price" : 6000}}
]

print(car_dicts)

# pop(key,"default")
del car_dicts[1]
print(car_dicts)

print()
print()

# 클래스 구조
# 구조 설계 후 재사용성 증가, 코드 반복 최소화, 메소드 활용

class Car():
    def __init__(self, company, details):
        self._company = company
        self._details = details

    def __str__(self):
        # print문으로 사용자 입장에서 출력을 원할때
        return "str : {} - {}".format(self._company,self._details)

    def __repr__(self):
        # 텍스트 뿐만 아니라 객체 정보도 표시해줌.
        return "repr : {} - {}".format(self._company, self._details)

car1 = Car("Ferrari", {"color" : "white" , "horsepower" : 400, "price" : 8000})
car2 = Car("Bmw", {"color" : "black" ,"horsepower" : 270,"price" : 5000})
car3 = Car("Audi", {"color" : "red","horsepower" : 300, "price" : 6000})
print(car1) # <__main__.Car object at 0x00CDE718>(원래는...) => __str__메소드 구현하면 속성정보를 원하는 방식으로 출력할 수 있음.
print(car2)
print(car3)

print(car1.__dict__)
print(car2.__dict__)
print(car3.__dict__)

print(dir(car1))

print()
print()

# 리스트 선언

car_list = []
car_list.append(car1)
car_list.append(car2)
car_list.append(car3)

print(car_list)

print()
print()

# 반복(__str__)
for x in car_list:
    print(x) # print로 출력할 때에는 str을 호출
