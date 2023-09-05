#Find the sum of all the multiples of 3 or 5 below the provided parameter value number.
multiples = []

def sumofmultiplesof3and5(number):
    for i in range(1, number):
        if i%3 ==0:
            if i not in multiples:
                multiples.append(i)
        elif i%5 ==0:
            if i not in multiples:
                multiples.append(i)
        else:
            i +=1
    #print(multiples)
    sum = 0
    count = 0
    while count < len(multiples):
        sum = sum + multiples[count]
        count += 1
    print(sum)
    


number = int(input("please enter number:> "))
sumofmultiplesof3and5(number)