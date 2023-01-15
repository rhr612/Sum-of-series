r=int(input('Define the range-\n'))
sum=0
for i in range(1,r+1):
    sum=sum+(i*i)
    print(i*i,end='')
    if i<r:
        print('+',end='')
print('= '+str(sum))

