class Vowels:
    def __init__(self,string):
        self.string=string
        self.index=0
    def __iter__(self):
        return self
    def __next__(self):
        while self.index < len(self.string):
            ch=self.string[self.index]
            self.index+=1
            if ch.lower() in "aeiou":
                return ch
        else:
            raise StopIteration
# s=Vowels("just thinking")
# l=iter(s)
# print(l)
# for c in s:
#     print(c,end=" ")

class Highest:
    def __init__(self,l):
        self.l=l
        self.index=0
        self.m=l[0]
    def __iter__(self):
        return self
    def __next__(self):
        if self.index < len(self.l):
            i=self.index
            self.index+=1
            if self.l[i] > self.m:
                self.m=self.l[i]
            return self.m
        else:
            raise StopIteration
obj= Highest([1,2,4,909,46,627,67,89])
for ch in obj:
    print(ch)
