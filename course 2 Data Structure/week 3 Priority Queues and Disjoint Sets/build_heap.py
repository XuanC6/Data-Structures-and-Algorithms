# python3

class HeapBuilder(object):
    def __init__(self):
        self.swaps = []
        self.data = []
    
    def ReadData(self):
        self.n = int(input())
        self.data = [int(s) for s in input().split()]
        assert self.n == len(self.data)
    
    def WriteResponse(self):
        print(len(self.swaps))
        for swap in self.swaps:
          print(swap[0], swap[1])
          
    def shift_down(self,i):
        min_index = i
        
        left_child_i = 2*i+1
        if left_child_i<self.n and self.data[left_child_i]<self.data[min_index]:
            min_index = left_child_i
        
        right_child_i = 2*i+2
        if right_child_i<self.n and self.data[right_child_i]<self.data[min_index]:
            min_index = right_child_i
        
        if i != min_index:
            self.data[i],self.data[min_index] = self.data[min_index],self.data[i]
            self.swaps.append((i, min_index))
            self.shift_down(min_index)
    
    def GenerateSwaps(self):
        for i in range(((self.n-1)//2)+1):
            j = (self.n-1)//2 -i
            self.shift_down(j)

    def Solve(self):
        self.ReadData()
        self.GenerateSwaps()
        self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
