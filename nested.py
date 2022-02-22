print("What type of cover does the book have?")
me = input()
if me == "soft":
    print("If the book is perfect-bound(Yes/No)?")
    me = input()
    if me == "yes":
        print("soft cover,perfect bound books are very popular")
    else:
        print("Soft covers with coils are great for short books")
else:
    print("Books with hard covers are expensive")



