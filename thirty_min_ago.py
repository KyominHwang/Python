#수호는 30분전으로 돌아가고 싶은 1인이다.
#공백을 기준으로 시간 분이 입력된다
#그러면 이 시간을 기준으로 30분 전의 시간을 출력하시오!
hour = int(input('몇시인지 입력하세요!(1~23)'))
minu = int(input('몇 분인지 입력하세요!(0~59)'))
def cal_time(a,b) :
    if b - 30 < 0 :
        a = a - 1
        b = b  + 30
    else :
         b = b - 30
    return a,b

print(cal_time(hour,minu))
