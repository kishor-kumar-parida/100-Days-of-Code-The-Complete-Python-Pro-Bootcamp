# # Error and Exception handling
# # try except else finally

# # file not found
# with open("demo.txt") as f:
#     data = f.readlines()
#     print(data)


# # KeyError
# a_dictionary = {"key":"value"}
# value = a_dictionary["non_exist_key"]


# # IndexError
# fruit_list = ["apple", "orange", "mango"]
# fruit = fruit_list[3]


# # TypeError
# text = "abc"
# print(text + 5)


# try:
#     file = open("demo.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["non_exist_key"])

# except FileNotFoundError:
#     file = open("demo.txt", "w")
#     file.write("Error and Exception handling")

# except KeyError as e:
#     print(f"The key {e} does not exist")

# else:
#     content = file.read()
#     print(content)

# finally:
#     if "file" in locals() and not file.closed:
#         file.close()
#         print("File closed")


# # raise exception
# height = float(input("height: "))
# weight = float(input("weight: "))

# if height > 3:
#     raise ValueError("height must be over 3 meters")

# bmi = weight / height**2
# print(bmi)
