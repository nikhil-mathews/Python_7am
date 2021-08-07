# 2i+6J
# 3i+6J+7K

class C2dVec:
    def __init__(self,i,j):
        self.icap=i
        self.jcap=j
    
    def display(self):
        print(f"{self.icap}i + {self.jcap}j")


class C3dVec(C2dVec):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.kcap=k
    def display(self):
        print(f"{self.icap}i + {self.jcap}j + {self.kcap}k")


v2d=C2dVec(2,3)
v2d.display()

v3d=C3dVec(1,2,3)
v3d.display()