# WAP to find out whether a post contains the word "Deergh"
# or not, and make it in such a way that it isn't case sensitive.

post = input("Enter Caption for Post: ")
name = 'Deergh'

# print(name.lower())
# print(post.lower())

# First, making both of them in lower case. So, we can compare them.
# Otherwise, the fact that string literals are case senstiive
# can create an issue.

name = name.lower()
post = post.lower()

if(name in post):
    print("Your name is present in the post!")
else:
    print("Your name isn't present in the post!") 
