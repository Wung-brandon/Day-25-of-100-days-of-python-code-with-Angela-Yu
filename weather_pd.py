import pandas as pd
import csv
""" 
with open("2.1 weather_data.csv") as data_file:
    data = csv.reader(data_file)
    #getting a column temp from a csv file and extracting the temp data and putting it into a new list called temperature
    temperatures = []
    for row in data:
        if row[1] != "temp": 
            temperatures.append(int(row[1]))
    print(temperatures) """
    
df = pd.read_csv("2.1 weather_data.csv")
#df_dict = df.to_dict()
#print(df_dict) 

temp_list = df["temp"].to_list()
temp = df["temp"] >= 15

#print(df[df.temp == df.temp.max()])
""" monday = df[df.day == "Monday"]
monday_temp = monday.temp
monday_temp_F = monday_temp * 9/5 + 32
print(f"{monday_temp_F}F" ) """
#print(temp)
#print(temp_list)
#add = sum(temp_list)
#div = add/len(temp_list)
data_dict = {
    "students": ["wung", "boris", "lucas", "besong"],
    "scores": [45,24,65,40]
}
data = pd.DataFrame(data_dict)
data.to_csv("new_file.csv")
#print(data)
""" 
print(f"the mean is {df['temp'].mean()}")
print(f"the mode is {df['temp'].mode()}")
print(f"the median is {df['temp'].median()}")
print(f"the standard deviation is {df['temp'].std()}")
print(f"the largest is {df['temp'].max()}")
print(f"the smallest is {df['temp'].min()}")
 """
#print(f"The average is {div}")
#print(type(df))
#print(df["temp"].shape)
#temp = df["temp"]
#print(temp.head(3))

#print(temp.max())
#print(temp) 
#df.info()
#print(df)
    


