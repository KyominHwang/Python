import urllib.request
import matplotlib.pyplot as plt

f = urllib.request.urlopen('http://www.textfiles.com/etext/FICTION/lesms10.txt').read()

dic = {}

list1 = f.split()
list2 = []
list_word = []
list_count = []
#print(list1)
for i in list1 :
    i = str(i)
    k = i[2:]
    k = k[:-1]
    list2.append(k)

for i in range(len(list2)):
    w = list2[i].upper()
    w = w.replace('.','').replace('?','').replace('!','').replace('"','').replace("'",'')
    if w not in dic :
        dic[w] = 1
    else :
        dic[w] += 1

for key in dic :
    list_word.append(key)
    list_count.append(dic[key])

a = sorted(list_count)
k = sum(list_count)
list = []
for i in a[-5:]:
    o = list_count.index(i)
    list.append(list_word[o])
def barchart(data,labels):
    num_bars = len(data)
    positions = range(1,num_bars + 1)
    plt.barh(positions, data, align='center')
    plt.yticks(positions, labels)
    plt.grid()
fig = plt.figure()
ax1 = fig.add_subplot(121)
barchart([a[-1],a[-2],a[-3],a[-4],a[-5]],[list[4],list[3],list[2],list[1],list[0]])
ax2 = fig.add_subplot(122)
labels = ['zip1','zip2','zip3','zip4','zip5']
sizes = [60,30,20,15,12]
barchart(sizes, labels)
plt.show()
