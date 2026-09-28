class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity # Variable for the capacity since the array is dynamic and is going to be changing 
        self.size = 0 
        self.arr = [0] * self.capacity #This is how we initialize the capacity of the array


    def get(self, i: int) -> int:
        return self.arr [i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n 
        

    def pushback(self, n: int) -> None:
        if self.capacity == self.size:
            self.resize()    
        self.arr[self.size] = n 
        self.size += 1 

    def popback(self) -> int:
        if self.size > 0: 
            self.size -= 1 
        #Soft deletion
        return self.arr[self.size]
 

    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        new_arr = [0] * self.capacity

        for i in range(self.size): 
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    def getSize(self) -> int:
        return self.size 
    
    def getCapacity(self) -> int:
        return self.capacity