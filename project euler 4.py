#Find the largest palindrome made from the product of two n-digit numbers
palindrome = False
mylist = []

#first, for each no of digits, the greatest is 999... etc so set this no aside (l)
#(for the greatest palindrome, we gon multiply largest nums and go down until we find a palindrome)
l="9"
z = int(input("enter no of digits "))

while len(l) < z:
    l = l + "9"
    print(l)
    
l = int(l)
y = l #1 less than greatest n digit number


        

while len(str(l)) == z:
    y = l
    palindrome = False
    while palindrome != True and len(str(y)) == z:
        prod = l*y
        new = str(prod)
        x = list(map(str, new))
        #print(x)
    #^ this splits the product into a string and puts it in the list x

        num = 0
        test = x[num]
        while num < len(x)-1:
            num = num + 1
            test = test + x[num]
        #print(test)

        i = len(x) -1
        test2 = x[i]
        while i > 0:
            i = i-1
            test2 = test2 + x[i]
            #print(test2)
        #^flips the product

        if test == test2:
            #print("palindrome")
            #print(test)
            #print(l)
            #print(y)
            palindrome = True
            mylist.append(int(test))
        else:
            y = y-1
 
    l = l-1

mylist.sort(reverse = True)
print(mylist[0])


#DONE