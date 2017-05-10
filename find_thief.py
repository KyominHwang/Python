#한적한 시골마을에 도둑이 들었다
#이 도둑은 마을의 재산을 훔쳐가다 마을 사람들에게 들켜 도망쳤다
#급하게 도망치느라 도둑은 신발이 벗겨졌다는 사실도 잊었다.
#마을 사람들은 도둑의 신발의 dna를 분석했다.
#도둑의 dna의 특징은 dna의 모든 숫자의 합을 7로 나눈 나머지가 4라는 사실을 알았다.
#다음날 경찰이 도둑으로 의심되는 사람을 검거하여 그들의 dna 샘플을 가져왔다.
#dna샘플을 분석하여 이 자가 도둑인지 아닌지를 판단하여 만약 도둑이면 suspect 아니면 citizen을 출력하는 프로그램을 만드시오

import random
n = int(input('input number'))
list = []
for i in range(n):
    list.append(random.randint(1,9))
b = sum(list)
c = b % 7
if c == 4 :
    print('suspect')
else :
    print('citizen')
