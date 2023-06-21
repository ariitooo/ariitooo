numbers = []
i = int(input('How many number? :'))
for i in range(i):
    n = int(input('enter a number :'))
    numbers.append(n)
d = int(len(numbers))
average = sum(numbers) / d
print(f" average is : {average}")

result = []
for num in numbers:
    if num > average:
        result.append(num)

print(result)
