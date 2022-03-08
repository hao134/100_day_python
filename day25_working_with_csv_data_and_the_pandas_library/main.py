# with open("weather_data.csv") as file:
#     data = file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))

# import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# average_temp = sum(temp_list) / len(temp_list)
# print(average_temp)
# #equal to
# print(data["temp"].mean())
#
# print(data["temp"].max())

# Get data in columns
#print(data["condition"])
# equal to
#data.condition

# get data in raw
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)
#
# # create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 65, 56]
# }
#
# data = pandas.DataFrame(data_dict)
# print(data)
#
# # save it
# data.to_csv()

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count  = len(data[data["Primary Fur Color"]== "Gray"])
red_squirrels_count  = len(data[data["Primary Fur Color"]== "Cinnamon"])
black_squirrels_count  = len(data[data["Primary Fur Color"]== "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")