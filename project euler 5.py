#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to n?

n= int(input("enter limit :> "))
current = n
list = []
Notsuccess = True
count = 0

while Notsuccess == True:
    for i in range(1,n+1):
        check = current%i
        if check == 0:
            list.append('y')
        else:
            list.append('no')
    if 'no' in list:
        current = current +1
        list.clear()
    else:
        print(current)
        Notsuccess = False


#DONEEEEEEEEEEEEE
