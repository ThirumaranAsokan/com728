print("What type of adventure should I have?")
me = input()
if (me == 'scary') or (me =='short'):
    print("Entering the dark forest\nif the type of adventure safe or long?")
    me = input()
    if (me =='safe') or (me == 'long') :
        print("Taking the safe route")
    else:
        print("Not sure which route to take")
else:
    print("Not sure which route to take")
