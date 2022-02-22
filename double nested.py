print("Where should I look?")
user = input()
if user=='in the bedroom':
    print("Where in the bedroom should i look?")
    user= input()
    if user == 'under the bed':
        print("Found some shoes but no battey")
    else:
        print("Found some mess but no battery")
if user == 'in the bathroom':
     print("where in the bathroom should i look?")
     user= input()
     if user == 'bathtub':
         print("Found the rubber duck but no battery")
     else:
         print("Found a wet surface but no battery")
if user == 'enters the lab':
     print("Where in the lab should I look?")
     user=input()
     if user == 'table':
        print("Yes I found my battery")
     else:
         print("Found some tools but no battery")



