graph={}
graph['start']={}
graph['start']['a']=5
graph['start']['b']=2
graph['a']={}
graph['a']['d']=4
graph['a']['c']=2
graph['b']={}
graph['b']['a']=8
graph['b']['c']=7
graph['c']={}
graph['c']['fin']=1
graph['d']={}
graph['d']['c']=6
graph['d']['fin']=3
graph['fin']={}

infinity=float('inf')
costs={}
costs['a']=5
costs['b']=2
costs['c']=infinity
costs['d']=infinity
costs['fin']=infinity

parents={}
parents['a']='start'
parents['b']='start'
parents['c']=None
parents['d']=None
parents['fin']=None

processed=[]

def find_lowest(costs):
    lowest_cost=float('inf')
    lowest_cost_node=None
    for node in costs:
        cost=costs[node]
        if cost<lowest_cost and node not in processed:
            lowest_cost=cost
            lowest_cost_node=node
    return lowest_cost_node

node=find_lowest(costs)
while node is not None:
    cost=costs[node]
    neighbors=graph[node]
    for n in neighbors.keys():
        new_cost=cost+neighbors[n]
        if costs[n]>new_cost:
            costs[n]=new_cost
            parents[n]=node
    processed.append(node)
    node=find_lowest(costs)

way=''
go='fin'
while parents[go]!='start':
    way+=' - '+parents[go]
    go=parents[go]
print('start - '+way[::-1]+'fin')
print('Fastest time in travel from start to fin is: ', costs['fin'])

print(graph)
