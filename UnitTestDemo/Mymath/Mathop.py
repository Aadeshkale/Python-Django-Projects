class math():
    def add(self,x,y):
        return x+y

    def sub(self,x,y):
        return x-y

    def mul(self,x,y):
        return x*y

    def div(self,x,y):
        return x//y

if __name__=="__main__":
    m=math()
    m.add(14,5)
    m.mul(12,13)
    print(m.sub(-2,-2))
