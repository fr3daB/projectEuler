# Find the difference between the sum of the squares of the first n natural numbers and the square of the sum
n = int(input("Enter the limit :> "))

#sum of squares:

added = 0
for i in range(n+1):
    square = i**2
    added = added +square

#square of sum
sum = 0
for i in range(n+1):
    sum = sum + i
sqofsum = sum**2

diff = abs(added - sqofsum)
print(diff)


#COMPLETE