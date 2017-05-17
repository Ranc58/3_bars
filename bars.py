import json
import sys
import math


def load_data(func):
    def wrapped(filepath, *args):
        try:
            with open(filepath, 'r') as file_handler:
                content_json = json.load(file_handler)
                sorted_by_seats = sorted(content_json,
                                         key=lambda seats: seats['SeatsCount'])
                func(sorted_by_seats, *args)
        except Exception as error:
            print('\n', error, '\n Error! Check JSON file and directory way\n')
            select_action_to_do()
    return wrapped


def select_action_to_do():
    input_way = input('Please enter way to JSON file: ')
    select_action = input('Please select what you want to do: '
                          '\n 1)Find smallest bar. '
                          '\n 2)Find biggest bar. '
                          '\n 3)Find closest bar'
                          '\n Or type "exit" to exit: ')
    if select_action == '1':
        get_smallest_bar(input_way)
    elif select_action == '2':
        get_biggest_bar(input_way)
    elif select_action == '3':
        try:
            longitude = input('Please enter longitude: ')
            latitude = input('Please enter latitude: ')
            get_closest_bar(input_way, float(longitude), float(latitude))
        except ValueError:
            print('Incorrect longitude and latitude! Enter correct values.')
            select_action_to_do()
    elif select_action == 'exit':
        print('GoodBye!')
        sys.exit()
    else:
        print("Error! Type correct variant!")
        select_action_to_do()


@load_data
def get_biggest_bar(sorted_by_seats):
    last_bar_in_list = len(sorted_by_seats)
    biggest_bar = sorted_by_seats[last_bar_in_list - 1]
    print('Список самых больших баров:')
    for bar in sorted_by_seats:
        if bar['SeatsCount'] == biggest_bar['SeatsCount']:
            print('%s имеет %s мест в зале.'
                  % (bar['Name'], bar['SeatsCount']))


@load_data
def get_smallest_bar(sorted_by_seats):
    smallest_bar = sorted_by_seats[0]
    print('Cписок самых маленьких баров:')
    for bar in sorted_by_seats:
        if bar['SeatsCount'] == smallest_bar['SeatsCount']:
            print('%s имеет %s мест в зале.'
                  % (bar['Name'], bar['SeatsCount']))


@load_data
def get_closest_bar(sorted_by_seats, longitude, latitude):
    my_coord = [[longitude, latitude]]
    coords_list = []
    for bar in sorted_by_seats:
        coords_list.append(math.sqrt((my_coord[0][0] -
                                      bar['geoData']['coordinates'][0]) ** 2 +
                                     ((my_coord[0][1] -
                                      bar['geoData']['coordinates'][1]) ** 2)))
        coords_list.append(bar['Name'])
        coords_list.append(bar['Address'])
    nearest_bar_coord = min(coords_list[::3])
    positiion_in_bar_coord_list = coords_list.index(nearest_bar_coord)
    print("Бар %s находится ближе всего к вам. Адрес: %s" % (
        coords_list.pop(positiion_in_bar_coord_list + 1),
        coords_list.pop(positiion_in_bar_coord_list + 1)))


if __name__ == '__main__':
    select_action_to_do()
