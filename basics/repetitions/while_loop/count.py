print("How many live cables must I avoid ?")
user = int(input())
a = 0
while a < user :
    print(' Avoiding...', end="")
    a = a + 1
    print(f"Done! {a} live cables avoided.")
