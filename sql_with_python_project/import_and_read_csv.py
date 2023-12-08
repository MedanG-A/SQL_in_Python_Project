import csv

def read_csv(csvfile):
    try:
        with open(csvfile) as csvfile:
            csvreader = csv.reader(csvfile, delimiter= ',')

            iris_list = list(csvreader)

    except FileNotFoundError:
        print("The file could not be found")
    except:
        print("An exception has occurred")
    finally:
        print("\n\nExecution complete. Closing the file")

