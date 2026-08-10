class student:
    def __init__(self,id,n,m):
        self.id=id
        self.name=n
        self.marks=m
    def __gt__(self, o):
        return self.marks > o.marks
    def __lt__(self, o):
        return self.marks < o.marks
    def __eq__(self, o):
        return self.marks == o.marks
    def __hash__(self):
        return hash(self.id)
    def __repr__(self):
        return self.name
s1=student(12,"raju",100)
s2=student(13,"raju",100)
s3=student(14,"soma",100)
print(s1>s2)
print(s1<s2)
print(s1==s2)
s={s1,s2,s3}
print(s)