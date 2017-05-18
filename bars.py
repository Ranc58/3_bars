import os
import json
import math


def load_data(func):
    def wrapped(filepath, *args):
        try:
            with open(filepath, 'r', encoding='windows-1251') as file_handler:
                content_json = json.load(file_handler)
                sorted_by_seats = sorted(content_json,
                                         key=lambda seats: seats['SeatsCount'])
                func(sorted_by_seats, *args)
        except Exception as error:
            print(error, '\nCheck JSON file content and way to file!')

    return wrapped


@load_data
def get_biggest_bar(sorted_by_seats):
    last_bar_in_list = len(sorted_by_seats)
    biggest_bar = sorted_by_seats[last_bar_in_list - 1]
    print('List of biggest bars:')
    for bar in sorted_by_seats:
        if bar['SeatsCount'] == biggest_bar['SeatsCount']:
            print('%s has %s seats in saloon.'
                  % (bar['Name'], bar['SeatsCount']))


@load_data
def get_smallest_bar(sorted_by_seats):
    smallest_bar = sorted_by_seats[0]
    print('List of smallest bars:')
    for bar in sorted_by_seats:
        if bar['SeatsCount'] == smallest_bar['SeatsCount']:
            print('%s has %s seats in saloon.'
                  % (bar['Name'], bar['SeatsCount']))


@load_data
def get_closest_bar(sorted_by_seats):
    try:
        longitude = input('Please enter Yours longitude: ')
        latitude = input('Please enter Yours latitude: ')
        my_coord = [[float(longitude), float(latitude)]]
    except ValueError:
        print('Incorrect longitude and latitude! Enter correct values.')
    else:
        shift_on_list = 1
        coords_list = []
        for bar in sorted_by_seats:
            diff_of_coords = math.sqrt((my_coord[0][0] -
                                        bar['geoData']['coordinates'][0])**2 +
                                       ((my_coord[0][1] -
                                         bar['geoData']['coordinates'][1])**2))
            coords_list.append(diff_of_coords)
            coords_list.append(bar['Name'])
            coords_list.append(bar['Address'])
        nearest_bar_coord = min(coords_list[::3])
        positiion_in_bar_coord_list = coords_list.index(nearest_bar_coord)
        print("%s is closest to you. Address: %s" % (
            coords_list.pop(positiion_in_bar_coord_list + shift_on_list),
            coords_list.pop(positiion_in_bar_coord_list + shift_on_list)))


if __name__ == '__main__':
    input_path = input('Please enter way to JSON file: ')
    select_action = input('Please select what you want to do: '
                          '\n 1)Find smallest bar. '
                          '\n 2)Find biggest bar. '
                          '\n 3)Find closest bar. ')
    if select_action == '1':
        get_smallest_bar(input_path)
    elif select_action == '2':
        get_biggest_bar(input_path)
    elif select_action == '3':
        get_closest_bar(input_path)
    else:
        print("Error! Type correct variant!")
