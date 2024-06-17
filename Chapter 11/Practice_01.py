# In this question, the detaisl except what inhertiance are
# not specified. So, we can assume it from our end.

class C2dVec:
    def __init__(self, i, j):
        self.icap = i
        self.jcap = j

    # We're creating an additional method to return
    # our vector in the desired output form
    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"

class C3dVec(C2dVec):
    def __init__(self, i, j, k):
        # We will use the super class constructor to bring the values
        # from the above 2D Vector Class.
        super().__init__(i, j)    
        self.kcap = k

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"

v2d = C2dVec(1, 3)
v3d = C3dVec(1, 7, 9)

print(v2d)
print(v3d)
