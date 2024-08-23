# def sum_list(lst):
#     # Base case: if the list is empty, return 0
#     if len(lst) == 0:
#         return 0
#     else:
#         # Recursive case: first element + sum of the rest of the list
#         return lst[0] + sum_list(lst[1:])
#
# # Example usage
# print(sum_list([1, 2, 3, 4, 5]))  # Output: 15
#############################


# def reverse_string(s):
#     # Base case: if the string is empty, return the empty string
#     if len(s) == 0:
#         return ""
#     else:
#         # Recursive case: last character + reverse of the remaining string
#         return s[-1] + reverse_string(s[:-1])
#
# # Example usage
# print(reverse_string("hello"))  # Output: "olleh"
##############################


# def power(base, exponent):
#     # Base case: any number to the power of 0 is 1
#     if exponent == 0:
#         return 1
#     else:
#         # Recursive case: base * (base raised to the power of (exponent-1))
#         return base * power(base, exponent -1)
#
# # Example usage
# print(power(2, 3))  # Output: 8
#################
##the use of dictionary##########
# dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
# words = ['cat', 'lion', 'horse']
#
# for word in words:
#     if word in dictionary:
#         print(word, "->", dictionary[word])
#     else:
#         print(word, "is not in dictionary")
#

###################tuple#########################
# my_tuple = (1, 2, True, "a string", (3, 4), [5, 6], None)
# print(my_tuple)
#
# my_list = [1, 2, True, "a string", (3, 4), [5, 6], None]
# print(my_list)

################# all about dictionary ########################
# colors = {
#     "white": [255, 255, 255,"hgf",0.8], #list in dictionary
#     "grey":[ 128, 128, 128],
#     # "red": (255, 0, 0), #tuple in dictionary
#     # "green": (0, 128, 0)
#     }
#
# for col, rgb in colors.items():
#     print(col, ":", rgb)

###########################
# for i in range(-1,2):
#     print("#")
list=[3,1,-1]
list[-1]=list[-2]
print(list)