a = [2, 4, 56, 7]

print(a[0] + a[1] + a[2] + a[3])
print(sum(a))

# You can use both of them.
# But, the second one is better.
# Moreover, you can also use for
# loops which will be seen ahead.

# For those who are curious how loops
# are used. Here's an example of for
# loops being used.

sum = 0
for i in range(len(a)):
    sum = sum + a[i]
print(sum)