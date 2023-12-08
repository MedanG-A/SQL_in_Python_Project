import pyodbc
import pandas as pd

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



results = cursor.execute("SELECT variety FROM iris_table GROUP BY variety;")
iris_df = pd.DataFrame(results)
print(iris_df)
