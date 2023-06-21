numbers = []
i=int(input('How many number? :'))
for i in range (i):
    n=int(input('enter a number :'))
    numbers.append (n)

for i in range(min(numbers), max(numbers)+1, 1):
    if i not in numbers:
        print(i)
