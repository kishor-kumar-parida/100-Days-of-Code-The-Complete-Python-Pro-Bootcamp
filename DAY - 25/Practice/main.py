# with open("weather_data.csv", mode="r") as data_file:
#     data = data_file.readlines()
#     print(data)

# ----------------------------------------------------------- #


# import csv
# with open("weather_data.csv", mode="r") as data_file:
#     data = csv.reader(data_file)
#     temp = []
#     for row in data:
#         if row[1] != "temp":
#             temp.append(int(row[1]))
#             print(row[1])
#     print(temp)

# ----------------------------------------------------------- #


# # pip install pandas
# import pandas

# data = pandas.read_csv("weather_data.csv")

# print(type(data))  # Data Frame - table
# print(type(data["temp"])) # series - column

# data_dict = data.to_dict()
# print(data_dict)  # Dictionary

# temp_list = data["temp"].to_list()
# print(temp_list)  # List -> [columns]

# print(data["temp"].max())
# print(data.temp.mean())


# # Get Data in columns
# print(data["day"])
# print(data.day)


# # Get Data in Rows
# print(data[data["day"] == "Monday"])
# print(data[data.day == "Monday"])

# # print the row foe max temperature
# print(data[data.temp == data.temp.max()])

# # Get the value need for row
# monday = data[data.day == "Monday"]
# monday_condition = monday.condition
# print(monday_condition)

# # Get the value need for row
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp.iloc[0])  # .iloc[0] -> for converting into intger
# monday_temp_f = monday_temp * 9 / 5 + 32
# print(monday_temp_f)


# # Create a dataframe from Scratch
# data_dict = {"students": ["kishor", "kumar", "Parida"], "Scores": [50, 60, 70]}

# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
# print(data)
