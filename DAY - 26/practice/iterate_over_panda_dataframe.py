import pandas

student_dict = {
    "student": ["kishor", "kumar", "parida", "som"],
    "score": [10, 20, 30, 40],
}


# # Looping through dictionary
# for (key, value) in student_dict.items():
#     print(value)


student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)


# # Looping through a data frame
# for (key, value) in student_data_frame.items():
#     print(key)


# # Looping through rows of data frames
# for index, row in student_data_frame.iterrows():
#     print(row.score)
