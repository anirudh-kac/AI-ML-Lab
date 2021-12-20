class Graph:
    
    def __init__(self,adjac_lis):
        self.adjac_list = adjac_lis
        
    def get_neighbour(self,v):
        return self.adjac_list[v]
    
    #Heuristic function
    def h(self,n):
        H = {
            'A' : 1,
            'B' : 1,
            'C' : 1,
            'D' : 1
        }
        
        return H[n]
    
    def a_star_algorithm(self,start,stop):
        
        open_list = set(start)
        closed_list = set()
        
        dist = {}
        dist[start] = 0
        
        prenode = {}
        prenode[start] = start
        
        while len(open_list) > 0 :
            n = None
            #print("Open list has " , len(open_list))
            
            
            #Find node with smallest value of dist(n) + h(n)
            for v in open_list :
                if n == None or dist[v] + self.h(v) < dist[n] + self.h(n):
                    n = v
            #print(n)
            
            if n == None :
                print('Path does not exist')
                return None
            
            #If stop node is found , create path and print
            if n == stop:
                reconst_path = []
                while prenode[n]!=n:
                    reconst_path.append(n)
                    n = prenode[n]
                    
                reconst_path.append(start)
                reconst_path.reverse()
                
                print('Path found : {}'.format(reconst_path))
                
                return reconst_path
            
            # For all neighbours of current node
            for m,weight in self.get_neighbour(n):
                
                # for a neighbour not visited first
                if m not in open_list and m not in closed_list:
                    #add to open list
                    open_list.add(m)
                    
                    #update prenode and distance
                    prenode[m] = n
                    dist[m] = dist[n] + weight
                else:
                    #if found and total distance is smaller , update
                    if dist[m] > dist[n] + weight:
                        dist[m] = dist[n] + weight
                        prenode[m] = n
                        
                        if m in closed_list : 
                            closed_list.remove(m)
                            open_list.add(m)
                        
            
            #Move current node from open to closed list
            open_list.remove(n)
            closed_list.add(n)

        print("Path does not exist !!!")
        return None
            
                        
                
                
        

# Adjacency list
adjac_list = {
    'A' : [('B',1),('C',3),('D',7)],
    'B' : [('D',5)],
    'C' : [('D',12)]   
}

graph1 = Graph(adjac_list)
graph1.a_star_algorithm('A','D') # A to D