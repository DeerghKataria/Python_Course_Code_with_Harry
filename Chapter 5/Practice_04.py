# This is a very important questions. From the perspective
# of output finding.

s = set()
s.add(20)
s.add(20.0)
s.add("20")

# So, we have s = {20, 20.0, "20"}

print(s)
print(len(s))