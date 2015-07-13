from Node import Node

class simple_agent_1:
    def __init__(self):
        #init 
        
        self.input = []
        self.init_input(32)
        
        self.output = []
        self.init_output(32)
        
        self.brain = []
        self.init_brain(64)
        
    def init_input(self,input_x):
        z = 1
        for i in range(1,input_x + 1):
            for j in range(1,input_x + 1):
                node = Node(i,j,z)
                self.input.append(node)
    
    def init_output(self,input_x):
        z = 1
        for i in range(1,input_x + 1):
            for j in range(1,input_x + 1):
                node = Node(i,j,z)
                self.output.append(node)
                
    def init_brain(self,input_x):
        z = 1
        for i in range(1,input_x + 1):
            for j in range(1,input_x + 1):
                node = Node(i,j,z)
                self.brain.append(node)
    
    def sense(self,input):
        self.input = input
        
    def think(self):
        #brain层，随机激活一小部分节点
        
        for i in self.brain:
            i.status = i.status
                
        
    def action(self):
        for i in self.output:
            i.status = 1
        
                
    def run_a_step(self):
       
        #每个节点，根据其他节点的状态调整与其他节点的权值
        #
        for i in self.input:
            for j in self.brain:
                if(i.status == 1 and j.status == 1):
                    if(j.id_str in i.connections):
                        i.connections[j.id_str] = i.connections[j.id_str]*1.1
                    else:
                        i.connections[j.id_str] = 0.1
                        
                    j.connections[i.id_str] = i.connections[j.id_str]
                    
                        
        for i in self.output:
            for j in self.brain:
                if(i.status == 1 and j.status == 1):
                    if(j.id_str in i.connections):
                        i.connections[j.id_str] = i.connections[j.id_str]*1.1
                    else:
                        i.connections[j.id_str] = 0.1
                        
                    j.connections[i.id_str] = i.connections[j.id_str]
                    