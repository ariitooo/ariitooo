a = int(input("Enter Number : "))
b = int(input("Enter Number : "))

if a > b:
    a, b = b, a

sm = 0

for i in range(a + 1, b, 1):
    sm = sm + i

print("Sum :", sm)
