import numpy as np
class Weight:
    def __init__(self,node,weight):
        #init
        self.node = node
        self.weight = weight
        
    def distance(self,node1,node2):
        a = np.array((node1.x,node1.y,node1.z))
        b = np.array((node2.x,node2.y,node2.z))
        return  np.linalg.norm(a-b)  