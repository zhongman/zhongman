names=['A','B','root','C','D']
message=input("Please tell me your name:")
if message=="root":
    print("Welcome, master, what can I do for you?")
elif message in names:
    print("Welcome "+message)
else:
    print("Wrong username.")
