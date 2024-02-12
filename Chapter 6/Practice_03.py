# This is for detecting spam, it can be used in endless ways.

text = input("Enter Text: ")
if("make a lot of money" in text):
    spam = True
elif("buy now" in text):
    spam = True
elif("click this" in text):
    spam = True
elif("subscribe this" in text):
    spam = True
else:
    spam = False
    

if(spam):
    print("This Text is SPAM!")
else:
    print("This Text isn't SPAM!")
