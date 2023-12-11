import csv
import pyodbc
import pandas as pd


def read_csv(csv_file):
    try:


s
with open(csv_file, newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    list_csv_data = list(csv_reader)
    print(list_csv_data)
except:
print("An error has occurred")

return list_csv_data

data = read_csv("iris.csv")
print(data[0])

server = 'localhost'
database = 'iris'
username = 'SA'
password = 'Chicken419'

docker_iris = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                             'SERVER=' + server +
                             ';DATABASE=' + database +
                             ';UID=' + username +
                             ';PWD=' + password)

cursor = docker_iris.cursor()
for title in data:
    header = data[0]
    rows = data[1:]
    print(rows[-1])
    cursor.execute(
        "INSERT INTO iris_data (sepal.length, sepal.width, petal.length, petal.width, variety) VALUES ({rows})")

"""
insert_stmt = (
  "INSERT INTO iris_data (sepal.length, sepal.width, petal.length, petal.width, variety)"
  "VALUES (%s, %s, %s, %s)"
)

"""

test = cursor.execute(insert_stmt)

# results = cursor.execute("""INSERT INTO iris_data (data[0])
#        VALUES (data[1:])""")
'''
docker_iris.commit()
iris_df = pd.DataFrame(results)
print(iris_df)
'''

