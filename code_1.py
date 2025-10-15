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


    def dfs(self, start, visited=None):
        if visited is None:
            visited = [False] * self.size

        visited[start] = True
        print(start, end=" ")

        for i in range(self.size):
            if self.matrix[start][i] == 1 and not visited[i]:
                self.dfs(i, visited)

    # BFS (в ширину) без deque
    def bfs(self, start):
        visited = [False] * self.size
        queue = [start]
        visited[start] = True

        while queue:
            vertex = queue.pop(0)  # забираємо перший елемент
            print(vertex, end=" ")

            for i in range(self.size):
                if self.matrix[vertex][i] == 1 and not visited[i]:
                    queue.append(i)
                    visited[i] = True
        
        
if __name__ == "__main__":
    g = graph(6)
    g.add_edge(0,1)
    g.add_edge(0,2)
    g.add_edge(1,3)
    g.add_edge(2,1)
    g.add_edge(3,4)
    g.add_edge(4,5)
    g.add_edge(1,5)
    g.add_edge(2,4)
    
    g.display()

    print("\nDFS starting from vertex 0:")
    g.dfs(0)

    print("\nBFS starting from vertex 0:")
    g.bfs(0)