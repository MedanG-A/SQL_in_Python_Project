import pyodbc
import pandas as pd
import csv

server = 'localhost,1433'
database = 'iris'
username = 'SA'
password = 'TheHairyOne1!'

# separate above sensitive details into separate file and gitignore
docker_iris = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                             'SERVER=' + server +
                             ';DATABASE=' + database +
                             ';UID=' + username +
                             ';PWD=' + password)
cursor = docker_iris.cursor()


def read_csv(csvfile):
    try:
        with open(csvfile, newline='') as csvfile:
            csv_read = csv.reader(csvfile, delimiter=',')

            csv_data_list = list(csv_read)

            return csv_data_list
            # iter_csv = iter(csv_read)
            #
            # next(iter_csv)
            #
            # for row in iter_csv:
            #     print(row[-1])

    except FileNotFoundError:
        print("File not found in the path location")


data_display = pd.DataFrame(read_csv("iris.csv"))

data_display = data_display.rename(columns={0: 'SepalLength', 1: 'SepalWidth', 2: 'PetalLength', 3: 'PetalWidth', 4: 'Variety'})

# sepal_length = data_display[0]
# sepal_width = data_display[1]
# petal_length = data_display[2]
# petal_width = data_display[3]
# variety = data_display[4]

# print(data_display)


for index, row in data_display.iterrows():
    cursor.execute("INSERT INTO iris_table (sepal_length, sepal_width, petal_length, petal_width, variety) "
                   "VALUES(?,?,?,?,?)", row.SepalLength, row.SepalWidth,
                   row.PetalLength, row.PetalWidth, row.Variety)

docker_iris.commit()

cursor.close()



