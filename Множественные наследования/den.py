def handle(request):
    global par
    if ':' in request:
        class1, class2 = map(str, request.split(' : '))
        for in_class2 in class2.split():
            if not par.get(in_class2, False):
                par[in_class2]=list()
            par[in_class2].append(class1)
    else:
        class1=str(request)
        if not par.get('main', False):
            par['main']=list()
        par['main'].append(class1)

def precheck(request):
    global par
    global res
    class1, class2 = map(str, request.split())
    if class1==class2:
        res.append('Yes')
        return
    if not class2 in str(par.values()):
        res.append('No1')
        return
    else:
        check(request)

def check(request):
    global par
    global res
    class1, class2 = map(str, request.split())
    for key,value in par.items():
        if (class1 in key) and (class2 in value):
            res.append('Yes')
            return True
    for key,value in par.items():
        if class2 in value:
            if key=='main':
                return
    for key,value in par.items():            
            if class2 in value:
                new_request=class1+' '+key
                l=check(new_request)
                if l:
                    return True

par={}
res=[]

n=int(input())
for i in range(n):
    handle(input())

print(par)

q=int(input())
for j in range(q):
    precheck(input())
    if len(res)!=j+1:
        res.append('No2')

for r in res:
    print(r)

print(len(res))

'''
3
B : A
C : A
D : B C
6
A B
B D
C D
D A 
A E
A A
'''

'''
2
A : C B
B : D E
1
E A 
'''
'''
11
Obj
A : Obj
B : Obj
C : Obj
F : A
K : A B
Z : B
G : C
L : F K
N : G
P : L Z N
13
A K
A A
Obj B
B P
N G
G L
Z P
P Z
Obj k
K B
K C
G Z
N P
'''