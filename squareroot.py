# Weekly task 6 

'''
Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.

You should create a function called <tt>sqrt</tt> that does this.

The aim is to create my own sqrt function and not to use the built in functions x ** .5 or math.sqrt(x).

This is to demonstrate that you can research and code a process (If you really needed the square root
 you would use one of the above methods). We will look at the newton method at estimating square roots. 

'''
# Ref:
# https://en.wikipedia.org/wiki/Newton's_method
# https://personal.math.ubc.ca/~anstee/math104/newtonmethod.pdf
# https://medium.com/@bundy01/newton-raphson-method-for-root-finding-in-python-6b1377103c4b
# https://www.oxfordlearnersdictionaries.com/definition/american_english/iteration
# https://en.wikipedia.org/wiki/Iteration

def sqrt(num):
    """Aroximates the square root of a positive floating-point number."""
     # Initial guess for the square root
    guess = num/ 2
    
    # Iterate untill the guess is close enough
    while abs(guess ** 2 - num) > 0.0001:
       guess = (guess + num / guess) / 2

    return guess

def main():
    """Main function."""
    # Enter a positive number
    num = float(input("please enter a positive number: "))

    # Check if the number is positive
    if num <= 0:
        print("Error: please enter a positive number:")
        return
    
    # Calculate the square root using the sqrt function
    result = sqrt(num)

    # Output the result
    print(f"The square root of {num} is approx. {result:.1f}.")

if __name__ == "__main__":
    main()

