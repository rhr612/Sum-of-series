r=int(input('Define the range-\n'))
sum=0
for i in range(1,r+1):
    sum=sum+i
    print(i,end="")

    if i<r:
        print('+',end="")
# print('\n')
# print('The sum of the series :')
print('= '+str(sum))

