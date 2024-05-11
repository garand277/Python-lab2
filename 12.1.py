from itertools import product
from itertools import repeat
count=0
letters = 'ШКОЛА' 
N=0
X=product(letters, repeat = 3)
for i in X:
    if ''.join(i).count('К')==1:
        N+=1
print(N)