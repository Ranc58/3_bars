import json
import math


def load_data_output_content(filepath):
    try:
        with open(filepath, 'r', encoding='windows-1251') as file_handler:
            return json.load(file_handler)
    except (ValueError, FileNotFoundError) as error:
        print(error, '\nIncorrect way or JSON file! Check it.')


def get_biggest_bar(content):
    biggest_bar = max(content, key=lambda seats: seats['SeatsCount'])
    print('%s has %s seats in saloon.\n' %
          (biggest_bar['Name'], biggest_bar['SeatsCount']))


def get_smallest_bar(content):
    smallest_bar = min(content, key=lambda seats: seats['SeatsCount'])
    print('%s has %s seats in saloon.\n' %
          (smallest_bar['Name'], smallest_bar['SeatsCount']))


def closest_bar(content, longitude, latitude):
    try:
        my_coord = [[float(longitude), float(latitude)]]
    except ValueError:
        print('Error! Incorrect longitude and latitude! Enter correct values.')
    else:
        for bar in content:
            diff_of_coords = math.sqrt((my_coord[0][0] -
                                        bar['geoData']['coordinates'][0])**2 +
                                       ((my_coord[0][1] -
                                         bar['geoData']['coordinates'][1])**2))
            bar['geoData']['coordinates'] = diff_of_coords
        closest_bar = min(content, key=lambda coords:
                          coords['geoData']['coordinates'])
        return closest_bar


def get_closest_bar(closest_bar):
    print("%s is closest to you. Address: %s" %
          (closest_bar['Name'], closest_bar['Address']))


if __name__ == '__main__':  # TODO Изменить входные параметры!
    input_path = input('Please enter way to JSON file: ')
    content = load_data_output_content(input_path)
    if content:
        longitude = input("Please enter longitude: ")
        latitude = input('Please enter latitude: ')
        print('Biggest bar: ')
        get_biggest_bar(content)
        print('Smallest bar: ')
        get_smallest_bar(content)
        print('Closest bar: ')
        closest_bar = closest_bar(content, longitude, latitude)
        if closest_bar:
            get_closest_bar(closest_bar)
