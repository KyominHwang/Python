import random

lotto_num_list = list(range(1,46))
random.shuffle(lotto_num_list)

for i in range(5):
 print(lotto_num_list[i])


