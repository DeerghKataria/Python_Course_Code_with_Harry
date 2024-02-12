class Sample:
    a = "Deergh"   
    
    def __init__(slf, name):
        slf.name = name
    
obj = Sample("Deergh")
print(obj.name)

# See, here in line 4. When we changed from 'self' to 'slf'
# Even though the code is working compeltely fine. 
# But, that's not something that we want. Because let's say
# if we hand over our code onto someone else. They would be 
# confused that why did we change 'self' to 'deergh'.

