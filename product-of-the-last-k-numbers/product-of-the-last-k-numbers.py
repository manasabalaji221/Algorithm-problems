class ProductOfNumbers:

    def __init__(self):
        self.arr=[]
        self.product = 1
        

    def add(self, num: int) -> None:
        if num==0:
            self.product=1
            self.arr=[]
        else:
            self.product*=num
            self.arr.append(self.product)
            
        
    def getProduct(self, k: int) -> int:
        n= len(self.arr)
        if n<k:
            return 0
        elif n==k:
            return self.arr[-1]
        else:
            return int(self.arr[-1] // self.arr[-1-k])
            


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)