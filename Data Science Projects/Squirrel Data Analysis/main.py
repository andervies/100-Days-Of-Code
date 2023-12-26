# import csv
import pandas

# with open("weather_data.csv", mode="r") as data_file:
#     data = data_file.readlines()
#     print(data)


# with open("weather_data.csv", mode="r") as data_file:
#     data = csv.reader(data_file)
#     print(data)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)
# import pandas
# data = pandas.read_csv("weather_data.csv")
# data_list = data["temp"]
# # average = sum(data_list)/len(data_list)
# # print(average)
# # print(data["temp"].max())
# #
# # print(data[data.temp == data["temp"].max()])
# monday = data[data.day == "Monday"]
# in_fahrenheit = monday.temp * 9/5 + 32
# print(in_fahrenheit)
data = pandas.read_csv("4.2 2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels = data[data['Primary Fur Color'] == "Gray"]
gray_squirrels_count = len(gray_squirrels)
red_squirrels = data[data['Primary Fur Color'] == "Cinnamon"]
red_squirrels_count = len(gray_squirrels)
black_squirrels = data[data['Primary Fur Color'] == "Black"]
black_squirrels_count = len(black_squirrels)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"], "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")