class Sample:
    a = "Deergh"   
    # This is a class attribute
    
obj = Sample()
obj.a = "Sam"
# This is an instance attribute.

print(Sample.a) # ---> Deergh
print(obj.a)    # ---> Sam