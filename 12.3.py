count=0
A=600000
while(count<5):
    A+=1
    for i in range(7,A):
        if i%10==7:
            if A%i==0 and i!=7:
                count+=1
                print(A,i)
                break