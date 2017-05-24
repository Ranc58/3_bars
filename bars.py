import json
import math


def load_data_output_content(filepath):
    with open(filepath, 'r', encoding='windows-1251') as file_handler:
        return json.load(file_handler)


def get_smallest_bar(content):
    smallest_bar = min(content, key=lambda seats: seats['SeatsCount'])
    return smallest_bar


def get_biggest_bar(content):
    biggest_bar = max(content, key=lambda seats: seats['SeatsCount'])
    return biggest_bar


def get_closest_bar(content, longitude, latitude):
    for bar in content:
        diff_of_coords = math.sqrt((longitude -
                                    bar['geoData']['coordinates'][0]) ** 2 +
                                   ((latitude -
                                     bar['geoData']['coordinates'][1]) ** 2))
        bar['geoData']['coordinates'] = diff_of_coords
    closest_bar = min(content,
                      key=lambda coords: coords['geoData']['coordinates'])
    return closest_bar


def print_smallest_bar(smallest_bar):
    print('Smallest bar: \n%s has %s seats in saloon.\n' %
          (smallest_bar['Name'], smallest_bar['SeatsCount']))


def print_biggest_bar(biggest_bar):
    print('Biggest bar: \n%s has %s seats in saloon.\n' %
          (biggest_bar['Name'], biggest_bar['SeatsCount']))


def print_closest_bar(closest_bar):
    print("%s is closest to you. Address: %s" %
          (closest_bar['Name'], closest_bar['Address']))


if __name__ == '__main__':
    input_path = input('Please enter way to JSON file: ')
    try:
        content = load_data_output_content(input_path)
        longitude = float(input("Please enter longitude: "))
        latitude = float(input('Please enter latitude: '))
    except (ValueError, FileNotFoundError):
        print('Error! Check input information and JSON file for correctness.')
    else:
        smallest_bar = get_smallest_bar(content)
        print_smallest_bar(smallest_bar)
        biggest_bar = get_biggest_bar(content)
        print_biggest_bar(biggest_bar)
        print('Closest_bar: ')
        closest_bar = get_closest_bar(content, longitude, latitude)
        print_closest_bar(closest_bar)
