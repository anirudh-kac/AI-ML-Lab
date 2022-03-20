def recAOStar(n):
    ##global finalPath
    print("Expanding Node : ",n)
    and_nodes = []
    or_nodes = []
    
    #Segregation of AND and OR
    
    if n in allNodes :
        if 'AND' in allNodes[n]:
            and_nodes = allNodes[n]['AND']
            
        if 'OR' in allNodes[n]:
            or_nodes = allNodes[n]['OR']
            
    #leaf node , return
    if len(and_nodes) == 0 and len(or_nodes)==0:
        return
    
    solvable = False
    marked = {}
    
    while not solvable:
        
        #if all child nodes visited and expanded, take the least  cost of all child nodes
        if len(marked) == len(and_nodes) + len(or_nodes):
            
            min_cost_least , min_cost_group_least = least_cost_group(and_nodes,or_nodes,{})
            solvable = True            
            change_heuristic(n,min_cost_least)
            optimal_child_group[n] = min_cost_group_least
            continue
        
        #Least cost of unmarked child nodes
        min_cost , min_cost_group = least_cost_group(and_nodes,or_nodes,marked)
        is_expanded = False
        
        #if child nodes have sub trees , then recursively visit all of the child nodes
        
        if len(min_cost_group) > 1:
            if min_cost_group[0] in allNodes:
                is_expanded = True
                recAOStar(min_cost_group[0])
                
            if min_cost_group[1] in allNodes:
                is_expanded = True
                recAOStar(min_cost_group[1])
                
        else:
                
            if min_cost_group in allNodes:
                is_expanded = True
                recAOStar(min_cost_group)
        
        #If child node has any subtree and expanded , verify new heuristic value is still smallest
        if is_expanded : 
            min_cost_verify , min_cost_group_verify = least_cost_group(and_nodes,or_nodes,marked)
            
            if min_cost_group == min_cost_group_verify :
                solvable = True
                change_heuristic(n,min_cost_verify)
                optimal_child_group[n] = min_cost_group
        #If child has no subtree , then no change in heuristic so update min cost
        else:
            solvable = True
            change_heuristic(n,min_cost)
            optimal_child_group[n] = min_cost_group
            
        marked[min_cost_group] = 1
            
    return heuristic(n)


def least_cost_group(and_nodes,or_nodes,marked):
    
    node_wise_cost = {}
    
    for node_pair in and_nodes:
        if not node_pair[0] + node_pair[1] in marked:
            cost = 0 
            cost = cost +  heuristic(node_pair[0]) + heuristic(node_pair[1]) + 2
            node_wise_cost[node_pair[0] + node_pair[1]] = cost
    
    for node in or_nodes:
        if not node in marked:
            cost = 0
            cost = cost + heuristic(node) + 1
            node_wise_cost[node] = cost
    
    min_cost = 9999
    min_cost_group = None
    
    for cost_key in node_wise_cost :
        if node_wise_cost[cost_key] < min_cost:
            min_cost = node_wise_cost[cost_key]
            min_cost_group = cost_key
            
    return [min_cost,min_cost_group] 

#return heuristics of a node

def heuristic(n):
    return H_dist[n]

def change_heuristic(n,cost):
    H_dist[n] = cost
    return

#function to print optimal cost nodes

def print_path(node):
    print(optimal_child_group[node],end = "")
    node = optimal_child_group[node]
    
    if len(node) > 1:
        if node[0] in optimal_child_group:
            print("->",end = "")
            print_path(node[0])
        
        if node[1] in optimal_child_group:
            print("->",end = "")
            print_path(node[1])
    else:
        if node in optimal_child_group:
            print("->",end = "")
            print_path(node)
            
#describe heuristic here
            
H_dist = {
    'A' : -1,
    'B' : 4,
    'C' : 2,
    'D' : 3,
    'E' : 6,
    'F' : 8,
    'G' : 2,
    'H' : 0,
    'I' : 0,
    'J' : 0
}
        

#describe graph here

allNodes = {
    'A' : {'AND' : [('C','D')],'OR' : ['B']},
    'B' : {'OR' : ['E','F']},
    'C' : {'OR' : ['G'],'AND' : [('H','I')]},
    'D' : {'OR' : ['J']}
}
    
optimal_child_group = {}

optimal_cost = recAOStar('A')

print("Nodes which give optimal costs are : ")

print_path('A')

print("Optimal cost is  : ",optimal_cost)