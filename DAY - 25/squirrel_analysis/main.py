import pandas

data = pandas.read_csv("squirrel_data.csv")

grey_count = len(data[data["Primary Fur Color"] == "Gray"])
red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "FurColor": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_count, red_count, black_count],
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
