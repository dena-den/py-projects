data=('1 5 2 7 1 9 3 8 5 9')
data=data.split(' ')
aver=0
num=0
while num<=(len(data)-1):
    aver+=int(data[num])
    num+=1
aver/=len(data)
print('Average is',aver)
e=0
for elem in data:
    elem=int(elem)
    e+=(elem-aver)**2
sigma=(e/(len(data)-1))**0.5
print(sigma)