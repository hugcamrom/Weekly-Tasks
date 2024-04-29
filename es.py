
'''
the-war-of-the-worlds.txt

Write a program that reads in a text file and outputs the number of e's it contains. Think about what is being asked here, 
document any assumptions you are making. The program should take the filename from an argument on the command line. 
It hasn't been shown how to do this, I need to look it up.

Marks will be given for dealing with errors eg no argument, filename that does not exist, or is not a text file.

'''



import random

# The allowed symbols.
symbols = " ABCDEFGHIJKLMNOPQRSTUVWXYZ "

# Randomly select k symbols from the string above.
L = random.choices(symbols, k=100)

# Show.
print(''.join(L))

# Open the book.
with open('data/thewaroftheworlds.txt', 'r', encoding='utf-8') as f:
    # Read the book into one long string
    text = f.read().upper()

    # Counts of the number of letters in the book.
    counts = {s: text.count(s) for s in symbols}



    # Show the number of E's.
    print("Number of 'E's:", counts['E'])
    
import sys
import os

def count_letters(text):
    """ Count the occurrences of each letter in the text."""
    symbols = " ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    counts = {s: text.count(s) for s in symbols}
    return counts

def main():
    """Main function."""
    # Check if a filename is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python es.py <filename>")
        return
    
    # Get the filename from the command-line argument
    file_name = sys.argv[1]
    
    # Check if the file exists
    if not os.path.exists(file_name):
        print("Error: File does not exist.")
        return
    
    # Check if the file is a text file
    if not file_name.endswith('.txt'):
        print("Error: Please provide a text file.")
        return
    
    # Open the file
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            text = f.read().upper()
    except Exception as e:
        print(f"Error: {e}")
        return
    
    # Count the occurrences of each letter in the text
    letter_counts = count_letters(text)
    
    # Output the result
    print("Counts of the number of letters in the book:")
    for letter, count in letter_counts.items():
        print(f"{letter}: {count}")

if __name__ == "__main__":
    main()