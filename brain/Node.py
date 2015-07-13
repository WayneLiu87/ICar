class Node:
    def __init__(self,x,y,z):
        #init
        self.status = 0
        self.x = x
        self.y = y
        self.z = z
        self.id_str = str(x) + "_" + str(y) + "_" + str(z)
        self.connections = dict()