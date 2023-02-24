# This is a python script to learn how to use CSV files
# https://docs.python.org/3/library/csv.html
import csv


def process_csv():
    # load from csv file
    with open('webform.csv', newline='') as f:
        reader = csv.reader(f)
        csv_data = list(reader)

    # simple print loaded csv row by row
    for row in csv_data:
        print(row)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    process_csv()


