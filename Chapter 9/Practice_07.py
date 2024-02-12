# This code is for finding where the word 'python' is present in it or not.

content = True  # ---> So, we can run it inside of the while loop.
i = 1

with open("log.txt") as f:
    while content:
        content = f.readline()
    
        if 'python' in content.lower():
            print(content)
            print(f"---> Yes, python is present on line number {i}\n")
        # else:
        #     print("No, python isn't present")
        i+=1
        