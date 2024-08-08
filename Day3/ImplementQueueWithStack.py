class MyQueue(object):
    def __init__(self):
        self.stackOne=[]
        self.stackTwo=[]
        
    def push(self, x):
        self.stackOne.append(x)
        

    def pop(self):
        self.shift()
        return self.stackTwo.pop()
        

    def peek(self):
        self.shift()
        return self.stackTwo[-1]
        

    def empty(self):
        return not self.stackOne and not self.stackTwo

    def shift(self):
        if not self.stackTwo:
            while self.stackOne:
                self.stackTwo.append(self.stackOne.pop())

def validateArr(action,num):
    q=MyQueue()
    ans=[]
    for x,y in zip(action,num):
        if x=="MyQueue":
            q=MyQueue()
            ans.append(None)
        elif x=="push":
            q.push(num[0])
            ans.append(None)
        elif x=="pop":
            ans.append(q.pop())
        elif x=="peek":
            ans.append(q.peek())
        elif x=="empty":
            ans.append(q.empty())
    return ans
        