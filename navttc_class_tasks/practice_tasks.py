# list=[1,2,3,4,5,6,7,8,9,10]
# for i in list:
#     if i%2==0:
#         print(i,'even number')
#     else:
#         print(i,'odd number')


#task2    this task iterates through a list of numbers and check if each number is prime
# Create a list of numbers from 1 to 10
numbers = []

for i in range(10):
    numbers.append(i + 1)

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Iterate through the list and check if each number is prime
for number in numbers:
    if is_prime(number):
        print(number, 'is a prime number')
    else:
        print(number, 'is not a prime number')




#task3 to find vowel words in sentence


# # Get a sentence from the user
# sentence = input("Enter any sentence: ")
#
# # Define a string of vowels
# vowels = "aeiouAEIOU"
#
# # Split the sentence into words
# words = sentence.split()
#
# # Initialize an empty list to hold words with vowels
# vowel_words = []
#
# # Check each word for vowels
# for word in words:
#     for char in word:
#         if char in vowels:
#             vowel_words.append(word)
#             break  # No need to check further once a vowel is found
#
# # Print the words that contain vowels
# print("Words containing vowels:", vowel_words)




