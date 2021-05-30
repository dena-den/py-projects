def create(namespace, parent):
    global namespaces
    l = namespaces.get(parent, False) #проверяет наличие ключа parent в словаре namespaceS и выводит значение по ключу
    if not l: #если l пустое, то
        namespaces[parent] = list() #в словарь namespaceS добавляется пара ключ parent - значение пустой список
        l = namespaces[parent] #l приравнивается значению по ключу parent в namespaceS
    l.append(namespace) #в l добавляется значение namespace


def add(namespace, var):
    global variables
    l = variables.get(namespace, False) #проверяет наличие ключа namespace в словаре variables и выводит значение по ключу
    if not l: #если l пустое, то
        variables[namespace] = list() #в словарь variables добавляется пара ключ namespace - значение пустой список
        l = variables[namespace] #l приравнивается значению по ключу namespace в variables
    l.append(var) #в l добавляется значение var


def get(namespace, var):
    global variables
    global namespaces
    result = None
    l = variables.get(namespace, False) #проверяет наличие ключа namespace в словаре variables и выводит значение по ключу 
    if not l or var not in l: #если l пустое или переменная var в него не входит, то
        for key, value in namespaces.items(): #для пары ключ-значение в кортеже пар из словаря namespaceS
            if namespace in value: #если namespace входит в значения value, то
                result = get(key, var) #запускает цикл заново и присваивает его значение переменной result
    else:
        result = namespace #иначе result равняется начальному namespace
    return result


def handle(request):
    global result
    command, arg1, arg2 = map(str, request.split())
    if command == 'create':
        create(arg1, arg2)
    elif command == 'add':
        add(arg1, arg2)
    elif command == 'get':
        result.append(get(arg1, arg2))


namespaces = {}
variables = {}

result = []

n = int(input())

for i in range(n):
    handle(input())

for r in result:
    print(r)


'''
Для проверки ввести в консоль:
9
add global a
create foo global
add foo b
get foo a
get foo c
create bar foo
add bar a
get bar a
get bar b
'''