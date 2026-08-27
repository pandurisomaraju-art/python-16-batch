from comparison import passwords


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
# obj= list_it([1,2,4,909,46,627,67,89])
# for i in obj:
#     print(i)

class user:
    def __init__(self,user,pas,ph):
        self.username=user
        self.pas=pas
        self.phoneno=ph
    def login(self):
        print("logged in")
    def logout(self):
        print("logged out")
class swiggy(user):
    pass
s1=swiggy("raju",14,4162782)
s1.login()
s1.logout()


class a:
    def m1(self):
        print("hello")
class b(a):
    def m2(self):
        print("bye")

# b1=b()
# b1.m1()
# b1.m2()