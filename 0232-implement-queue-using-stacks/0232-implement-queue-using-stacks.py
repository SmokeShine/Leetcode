class MyQueue:

    def __init__(self):
        self.stack1=[]
        self.stack2=[]

    def push(self, x: int) -> None:
        if len(self.stack1)<10:
            #use stack2
            self.stack1.append(x)
        else:
            self.stack2.append(x)

    def pop(self) -> int:
        if not self.stack1:
            #use stack2
            temp=self.stack2[0]
            self.stack2=[self.stack2[i] for i in range(1,len(self.stack2))]
        
        else:
            temp=self.stack1[0]
            self.stack1=[self.stack1[i] for i in range(1,len(self.stack1))]
        return temp

    def peek(self) -> int:
        if self.stack1:
            return self.stack1[0]
        return self.stack2[0]

    def empty(self) -> bool:
        if not self.stack1 and not self.stack2:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()