#파일 읽기, 쓰기
#읽기 모드 : r, 쓰기모드(기존 파일 삭제):w, 추가모드(파일 생성또는 추가):a
#.. : 상대경로, . : 절대경로

#파일읽기
#ex1
f = open('./resource/review.txt','r')
content = f.read()
print(content)
print(dir(f))#사전 같은 역할을 하는 함수
#반드시 close로 리소스 반환
f.close()

#예제2
#close를 해주지 않아도 됨
with open('./resource/review.txt','r') as f : #f = open('./resource/review.txt','r')
  c = f.read()
  print(c)
  print(list(c))
  print(liter(c))#for문에서 사용 가능
  
#예제3
with open('./resource/review.txt','r') as f:
  for c in f:
    print(c.strip) #라인 단위로 출력
    #strip : 공백을 없애준다.
    
#예제4
with open('./resource/review.txt','r') as f:
  content = f.read()
  print(">",content)#내용이 출력됨
  content = f.read()#내용 없음
  print(">",content)#내용이 출력되지 않음.
  
#예제5
with open('./resource/review.txt','r') as f:
  line = f.readline()
  #print(line) #한줄만 출력함
  while line :
    print(line, end='####')
    line = f.readline()#한줄 단위로 읽음
    
#예제6
with open('./resource/review.txt','r') as f:
  content = f.readlines()
  print(content)#escape문자를 포함해서 출력, 리스트 형태로
  for c in content:
    print(c,end=r'%%%%%%%')
    
#예제7
with open('./resource/score.txt','r') as f:
  score = []
  for line in f:
    score.append(int(line))
  print(sum(score)/len(score))
  
  
#파일쓰기

#예제1
with open('./resource/text1.txt','w') as f:
  f.write('niceman\n')
  

#예제2
with open('./resource/text1.txt','a') as f:
  f.write('goodman')
  
#예제3
from random import randint
with open('./resource/text2.txt','w') as f:
  for cnt in range(6):
    f.write(str(randint(1,100)))
    f.write('\n')

#예제4
#writelines:리스트 -> 파일로 저장
with open('./resource/text3.txt','w') as f:
  list = ['kim\n','park\n','joe\n']
  f.writelines(list)
  
#예제5
with open('./resource/text4.txt','w') as f:
  print('Test contests1!',file = f)#바로 파일에 저장함.
  

  
