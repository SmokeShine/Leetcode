class TwoSum:

    def __init__(self):
        self.array=[]

    def add(self, number: int) -> None:
        self.array.append(number)

    def find(self, value: int) -> bool:
        seen=set()
        for i in self.array:
            if value-i in seen:
                return True
            else:
                seen.add(i)
        return False
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)