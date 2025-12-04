gword=input("there is a word the computer wants. guess that word")
word="stop"
NoOfAttempts=0
done=False
while done==False:
    if gword==word:
        print("you got it! your attempt count",NoOfAttempts)
        done = True
    else:
        print("nope")
        NoOfAttempts=NoOfAttempts+1