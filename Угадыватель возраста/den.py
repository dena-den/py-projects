def age():
    down=0
    up=100
    ans=''
    while ans!='y':
        n=(up+down)//2
        ans=input('Is your age {}? '.format(int(n)))
        if ans=='m':
            down=n
        elif ans=='l':
            up=n
    print('Your age is {}'.format(n))
            
age()
            
