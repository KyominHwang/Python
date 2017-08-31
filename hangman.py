import os
print('input the answer of the hangman')
answer = input()
os.system('clear')
print('this is hangman. insert only one letter in here!')

list2 = []

for i in range(len(answer)) :
        list2.append(answer[i])

count = 0
#correct = 0
list3 = []
for i in range(len(answer)):
    list3.append("_")
while count < 10 :
    a = input('input one letter here : ')
    if a in list2 :
        for i in range(len(answer)):
            if a == list2[i]:
                list3[i] = a
                #count += 1
        print(list3)
        if not('_' in list3):
            print('you correct the answer!')
            break
    else :
        #count = count + 1
        print(list3)
    count = count + 1
if count == 10 :
    print("you didn't correct the answer!")
