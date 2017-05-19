import json
import math


def load_data_output_content(filepath):
    try:
        with open(filepath, 'r', encoding='windows-1251') as file_handler:
            return json.load(file_handler)
    except FileNotFoundError as error:
        print(error, '\nIncorrect way to JSON file! Check it.')


def sort_content(content):
    try:
        sorted_by_seats = sorted(content,
                                 key=lambda seats: seats['SeatsCount'])
        return sorted_by_seats
    except Exception:
        print('Incorrect JSON file! Check it.')


def get_biggest_bar(sorted_by_seats):
    list_bars_seats = []
    for bar in sorted_by_seats:
        list_bars_seats.append((bar['SeatsCount'], bar['Name']))
    smallest_bar = max(list_bars_seats)
    print('%s has %s seats in saloon.\n' % (smallest_bar[1], smallest_bar[0]))


def get_smallest_bar(sorted_by_seats):
    list_bars_seats = []
    for bar in sorted_by_seats:
        list_bars_seats.append((bar['SeatsCount'], bar['Name']))
    smallest_bar = min(list_bars_seats)
    print('%s has %s seats in saloon.\n' % (smallest_bar[1], smallest_bar[0]))


def get_closest_bar(sorted_by_seats, longitude, latitude):
    try:
        my_coord = [[float(longitude), float(latitude)]]
    except ValueError:
        print('Error! Incorrect longitude and latitude! Enter correct values.')
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
    content = load_data_output_content(input_path)
    if content:
        longitude = input('Please enter Yours longitude: ')
        latitude = input('Please enter Yours latitude: ')
        sorted_by_seats = sort_content(content)
        if sorted_by_seats:
            print('Biggest bar: ')
            get_biggest_bar(sorted_by_seats)
            print('Smallest bar: ')
            get_smallest_bar(sorted_by_seats)
            print('Closest bar: ')
            get_closest_bar(sorted_by_seats, longitude, latitude)
