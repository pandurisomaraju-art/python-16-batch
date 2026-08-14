class list_it:
    def __init__(self,l):
        self.l=l
        self.index=0
    def __iter__(self):
        return self
    def __next__(self):
        while self.index<len(self.l):
            i=self.index
            self.index+=1
            if self.l[i]%2==0:
                return self.l[i]
        else:
            raise StopIteration
obj= list_it([1,2,4,909,46,627,67,89])
for i in obj:
    print(i)
