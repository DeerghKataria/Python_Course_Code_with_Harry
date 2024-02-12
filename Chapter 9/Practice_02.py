def game():
    return 10

score = game()
with open("highscore.txt") as f:
    high_score = int(f.read())
    
if high_score == '':
    with open("highscore.txt", "w") as f:
        f.write(str(score))
elif int(high_score) < score:
    with open("highscore.txt", "w") as f:
        f.write(str(score))
        
# After running this code check the .txt file and the changes would be made over there.
        
