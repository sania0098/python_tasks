import string


def count_letters(filename):
    letter_count = {letter: 0 for letter in string.ascii_lowercase}  # Initialize counts for all letters

    try:
        with open(filename, 'r') as file:
            content = file.read()  # Read the entire file content
            for char in content:
                if char.isalpha():  # Check if the character is a letter
                    letter_count[char.lower()] += 1  # Convert to lowercase and count

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return

    # Print histogram
    print("Letter Frequency Histogram:")
    for letter in sorted(letter_count):
        count = letter_count[letter]
        if count > 0:
            print(f"{letter}: {count}")


# Create a test file
with open('test.txt', 'w') as test_file:
    test_file.write('aBc')

# Ask user for input file name
input_filename = input("Enter the name of the input file: ")
count_letters(input_filename)
