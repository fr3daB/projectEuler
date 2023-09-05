#fibonacci sequence
#By considering the terms in the Fibonacci sequence whose values do not exceed n, find the sum of the even-valued terms
x = 1
y = 2

n = int(input(" Enter a limit:> "))

sequence = [x, y]
next = sequence[len(sequence)-1] + sequence[len(sequence)-2]

while next<=n:
    sequence.append(next)
    next = sequence[len(sequence)-1] + sequence[len(sequence)-2]
print(sequence)

sum = 0
for i in sequence:
    if i%2 == 0:
        sum = sum + i
print(sum)