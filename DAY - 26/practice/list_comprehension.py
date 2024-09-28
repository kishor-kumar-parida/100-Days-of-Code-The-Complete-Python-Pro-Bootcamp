# # List Comprehension
# # new_list = [new_item for item in list]
# # dd_one = [item+1 for item in old_list]

# numbers = [1, 2, 3]
# add_one = [item + 1 for item in numbers]
# print(numbers)
# print(add_one)

# # String Comprehension
# name = "kishor"
# new_list = [letter for letter in name]
# print(new_list)

# # Range Comprehension
# list = [num * 2 for num in range(1, 5)]
# print(list)


# # Conditional List Comprehension
# # new_list = [new_item for item in list if test]

# names = ["kishor", "Kumar", "Parida", "som"]
# new_names = [name for name in names if len(name) <= 5]
# print(new_names)

# names = ["kishor", "Kumar", "Parida", "som"]
# new_names = [name.upper() for name in names if len(name) > 5]
# print(new_names)


# #
# # Exercise
# # file1 = [1,2,3]
# # file2 = [2,3,4]
# # output = [2,3]

# with open("file1.txt") as file1:
#     file_1_data = file1.readlines()

# with open("file2.txt") as file2:
#     file_2_data = file2.readlines()

# result = [int(num) for num in file_1_data if num in file_2_data]

# print(result)
