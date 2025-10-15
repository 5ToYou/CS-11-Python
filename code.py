class graph:
    def __init__(self,size,):
        self.matrix = []
        self.size = size
        for i in range (size):
            self.matrix.append([0 for i in range(size)])

        
    def add_edge(self,v1,v2):
        if v1 == v2:
            print("its the same %d and %d" % (v1,v2))
        self.matrix[v1][v2] = 1
        self.matrix[v2][v1] = 1
        
    def remove_edge(self,v1,v2):
        if self.matrix[v1][v2] == 0:
            print(f"No edge between {v1} & {v2}")
        self.matrix[v1][v2] = 0
        self.matrix[v2][v1] = 0
        
    def display(self):
        for row in self.matrix:
            for val in row:
                print(val,end=" "),
            print()
        
        
if __name__ == "__main__":
    g = graph(5)
    g.add_edge(0,3)
    g.add_edge(0,1)
    g.add_edge(0,2)
    g.add_edge(1,2)
    
    g.display()