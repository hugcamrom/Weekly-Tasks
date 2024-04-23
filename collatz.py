# Weekly task 4

# Write a program, called collatz.py, that asks the user to input any positive integer 
# and outputs the successive values of the following calculation.
# At each step calculate the next value by taking the current value and, if it is even, divide it by two, 
# but if it is odd, multiply it by three and add one.
# Have the program end if the current value is one.

def collatz(num):
    while(num!=1):
        if(num%2==0):
            num=num//2
            print(num)
        else:
            num=3*num+1
            print(num)

numx= int(input("Enter number:\n"))
collatz(numx)

