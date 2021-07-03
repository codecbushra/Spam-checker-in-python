message=input("Enter any message here:\n")
spam_msg=['make a lot of money', 'buy now', 'subscribe this', 'click this']
for i in spam_msg:
    if i in message:
        spam=True
        break
    else:
        spam=False
        
if(spam):
    print("This message look's like a spam")
else:
    print("This is not a spam message")
