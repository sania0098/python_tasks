# def dic():
#     student_data = {"name": "Ali", "F_name": "asad", "email": "ali00@gmail.com",
#                     'class':9,'section':'B','subject':"arts"}
#     data_check = ['cat', 'name', 'class','subject','email']
#
#     for word in data_check:
#         if word in student_data:
#             print(word, "->", student_data[word])
#         else:
#             print(word, "is not in student data")
# dic()


# the concept of keys in dictionary
# def key_dic():
#     student_data = {"name": "Ali", "F_name": "asad", "email": "ali00@gmail.com",
#                     'class': 9, 'section': 'B', 'subject': "arts"}
#     for key in student_data.keys():
#          print(key, "->", student_data[key])
# key_dic()


# the use of sorted function
# def sorted_key_dic():
#     student_data = {"name": "Ali", "F_name": "asad", "email": "ali00@gmail.com",
#                     'class': 9, 'section': 'B', 'subject': "arts"}
#     for key in sorted(student_data.keys()):
#          print(key, "->", student_data[key])
# sorted_key_dic()


# the concept of items
# def items_dic():
#     student_data = {"name": "Ali", "F_name": "", "email": "ali00@gmail.com",
#                     'class': 9, 'section': 'B', 'subject': "arts"}
#     for statement,data in student_data.items():
#         print(statement, "->", data)
# items_dic()

# select onlt values only
# def values_dic():
#     student_data = {"name": "Ali", "F_name": "", "email": "ali00@gmail.com",
#                     'class': 9, 'section': 'B', 'subject': "arts"}
#     for data in student_data.values():
#         print( "->", data)
# values_dic()


       #modification and addition of new values

student_data = {"name": "Ali", "F_name": "", "email": "ali00@gmail.com",
                    'class': 9, 'section': 'B', 'subject': "arts"}
student_data["name"]='sara' #modify
print('dictionary after modification',student_data)
student_data['roll_no']=12

student_data.update({'phone_num':'08767234'})
print('dictionary after updation',student_data)
del student_data['class']
print('dictionary after del key',student_data)
student_data.popitem()
print('after popitem',student_data)


