#finding the largest prime factor
number = int(input("Enter your number:> "))

i=2

while i<=number:
    if number%i==0:
        primelarger = i
        while number%i==0:
            number = number/i
    i +=1
print(primelarger)


    
    