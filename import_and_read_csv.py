import csv

def read_csv(csvfile):
    try:
        with open(csvfile) as csvfile:
            csvreader = csv.reader(csvfile, delimiter= ',')
            row_list = []

            iris_iter = iter(csvreader)
            next(iris_iter)
            for row in iris_iter:
                row_list.append(row)

            return row_list

    except FileNotFoundError:
        print("The file could not be found")
    except:
        print("An exception has occurred")
    finally:
        print("\n\nExecution complete. Closing the file")

