def solution(roman):
    num=dict({'M': 1000, 'D': 500, 'C':100, 'L': 50, 'X': 10, 'V': 5, 'I':1})
    roman=list(roman)
    for item in roman:
        if item in num:
            roman[roman.index(item)]=num[item]
    sum=0
    while len(roman)>1:
        if roman[0]>=roman[1]:
            sum+=roman.pop(0)
        else:
            sum+=(roman.pop(1)-roman.pop(0))
    if len(roman)==1:
        sum+=roman.pop(0) 
    return sum

x = input('Введите римское число:')
if x:
    print(solution(x))