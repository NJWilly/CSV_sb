# This is a python script to learn how to use CSV files
# https://docs.python.org/3/library/csv.html
import csv
import string


name_allowed_s = list(string.ascii_uppercase) + list(string.ascii_lowercase) + ['\'', ' ', '-', '.', 'í']
title_allowed_s = list(string.ascii_uppercase) + list(string.ascii_lowercase) + ['\'', ' ', '-', '.', 'í', '/', ',']

def process_csv():
    # load from csv file
    with open('webform.csv', newline='') as f:
        reader = csv.reader(f)
        csv_data = list(reader)

    # save header row
    fixed_data = []
    fixed_data.append(csv_data[0])

    # loop through the loaded csv one row at a time
    for row in csv_data:

        # strip leading and trailing whitespace from all fields
        for data_item in row:
            data_item = data_item.strip()

        # we only care if the person is attending
        if row[11] == 'I Will Attend':

            # Flag if first or last name is in all caps or all lower
            if row[1].isupper() or row[2].isupper() or row[1].islower() or row[2].islower():
                print(f'\nproblem with name formatting: '
                      f'{row[3]}, {row[2]} - corrected to {row[3].capitalize()}, {row[2].capitalize()}')
                row[3] = row[3].capitalize()
                row[2] = row[2].capitalize()

            # check if there are any funny characters in the name
            if not all(ch in name_allowed_s for ch in row[3] + row[2]):
                print(f'\n{row[3]}, {row[2]} has a funny character in their name')

            # check if their title is empty
            if len(row[4]) == 0:
                row[4] = input(f'\n{row[3]}, {row[2]} has no title.  Enter their title: ')

            # check if there are any funny characters in the title
            if not all(ch in title_allowed_s for ch in row[4]):
                print(f'\n{row[3]}, {row[2]} has a funny character in their title - {row[4]}')

            # check if there are too many commas in their title
            if row[4].count(',') > 1:
                row[4] = input(f'\n{row[3]}, {row[2]} has too many commas in their title.  {row[4]} '
                               f'Perhaps they listed their credential instead? Enter corrected title: ')
            fixed_data.append(row)

    # output csv file
    with open('webform-fixed.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(fixed_data)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # fix data
    process_csv()

    # TODO: create list of dietary restrictions
    #
    # TODO: assign table numbers




