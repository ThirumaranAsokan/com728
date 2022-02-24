print("How many numbers should i sum?")
user = int(input())
a = 1
total = 0
while a<=user:
    print(f"Please enter number {a} of 4:")
    total += int(input())
    a = a + 1

print("The answer is",total)

