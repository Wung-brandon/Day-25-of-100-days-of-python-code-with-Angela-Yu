import pandas as pd


df = pd.read_csv("4.3 2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#print(df.head(10))
#print(df.tail(10))
#print(df.shape)

#pd.set_option('display.max_columns', None)
#pd.set_option('display.max_rows', None)

#print(df.head())

df1 = df["Primary Fur Color"]
#print(df1)
gray_count = df1[df["Primary Fur Color"] == "Gray"].count()
print(f"The number of gray squirrels is {gray_count}")

cinnamon_count = df1[df["Primary Fur Color"] == "Cinnamon"].count()
print(f"The number of cinnamon squirrels is {cinnamon_count}")

black_count = df1[df["Primary Fur Color"] == "Black"].count()
print(f"The number of black squirrels is {black_count}")

color = {
    "Fur Color":["Gray","Cinnamon","Black"],
    "Count": [gray_count,cinnamon_count,black_count]
}
data = pd.DataFrame(color)
data.to_csv("Fur_color_file.csv")
#print(data)
