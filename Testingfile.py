
import pandas as pd
data = pd.read_csv("D:\\Study\\WorldQuat Data Science\\Data\\brasil-real-estate-2.csv", encoding = 'latin1')
#print(data.head()) #print the first five rows of the data.
print(data.index[:5]) #This retrieves the index of the DataFrame, which is essentially the row labels. By default, the index is an integer-based range starting from 0. [:5] Slices notation selects the first five elements of the index.
print(data.shape) #To tell the data shape of the dataframe(the number of rows and columns).
print(data.head()) #Print the first five rows of the data.
print(data.loc[2]) #print the third row of the data
print(data["state"]) #Access the column name using the column name as the key.
print(data.state) #Access the column by the use of the column name.
print(data[["state", "region", "lat"]]) #Accessing the multiple column from the data.
print(data.loc[:, "state"]) #Access the column using loc function
print(data.iloc[:, 1]) #Access the column using the function .iloc
print(data.loc[3:10]) #Access the rows for the third to tenth
print(data.columns) #checking for the dataframe columns
print(data.size)
print(data.tail()) #print the last five rows in a data

dictionary = {"names": ["Anto", "Toni", "Tonito"],
"Ages" : [44, 24, 53],
"State" : ["New york", "LA", "Chicago"]
}
dictionary1 = pd.DataFrame(dictionary)
print(dictionary1)
print(dictionary1.loc[2, "Ages"])
print(dictionary1.iloc[:, [1,1]])
print(data.info()) # info() function tells all sorts of things about the data.
print(data.sort_values("lat"))#

print(data.set_index("state").sort_index().tail())