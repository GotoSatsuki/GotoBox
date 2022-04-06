import numpy as np

loop_n = int(input('ループ回数を入力しろ>>>'))
counter = 0

# main

for i in range(loop_n):
    x = np.random.uniform(0, 1)
    y = np.random.uniform(0, 1)
    if(x*x+y*y < 1):
        counter +=1
    print(i+1, 4*counter/(i+1))