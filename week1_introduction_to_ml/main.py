import pandas as pd

file_path = '/home/felipesantos/Downloads/iris.data'

iris_data = pd.read_csv(file_path)

#print(iris_data.head())
print(iris_data.info())

print(iris_data.shape)