# Dictionary Comprehension
# new_dict = {new_key: new_value for item in list}


# import random

# names = ["kishor", "Kumar", "Parida", "Som"]
# students_score = {student: random.randint(1, 10) for student in names}
# print(students_score)

# # {'kishor': 7, 'Kumar': 1, 'Parida': 4, 'Som': 8}


# # passed_students = {new_key:new_value for(key,value) in dictionary.items()}
# passed_students = {
#     student: score for (student, score) in students_score.items() if score >= 6
# }
# print(passed_students)


# # Excersise - 1
# sentence = "My name is Kishor Kumar Parida"
# result = {word: len(word) for word in sentence.split()}
# print(result)


# # Excersise - 2
# weather_c = {
#     "monday": 12,
#     "tuesday": 14,
#     "wednesday": 15,
#     "thursday": 14,
#     "friday": 21,
#     "saturday": 22,
#     "sunday": 24,
# }

# result = {days: value * 9 / 5 + 32 for (days, value) in weather_c.items()}
# print(result)
