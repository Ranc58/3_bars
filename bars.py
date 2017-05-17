import json
import sys


def load_data(func):
    def wrapped(filepath, *args):
        try:
            with open(filepath, 'r') as file_handler:
                content_json = json.load(file_handler)
                sorted_by_seats = sorted(content_json,
                                        key = lambda seats: seats['SeatsCount'])
                func(sorted_by_seats, *args)
        except Exception as error:
            print('\n',error,'\n Error! Check JSON file and directory way\n')
            select_action_to_do()
    return wrapped


def select_action_to_do():
    select_action = input('Please select what you want to do: '
                          '\n 1)Find smallest bar. '
                          '\n 2)Find biggest bar. '
                          '\n 3)Find closest bar'
                          '\n Or type "exit" to exit: ')
    if select_action != 'exit':
        input_way='d:/pycharmprj/3_bars/bars.json'
        #input_way = input('Please enter way to JSON file: ')
        if select_action == '1':
            get_smallest_bar(input_way)
        elif select_action == '2':
            get_biggest_bar(input_way)
        elif select_action == '3':
            longitude = input('Please enter longitude: ')
            latitude = input('Please enter latitude: ')
            get_closest_bar(input_way, float(longitude), float(latitude), )
    else:
        print('GoodBye!')
        sys.exit()


@load_data
def get_biggest_bar(sorted_by_seats):
    result = sorted_by_seats.pop()
    for bar in sorted_by_seats:
        if bar['SeatsCount'] == result['SeatsCount']:
            print('%s имеет %s мест в зале. '
                'Это один из самых больших баров в списке.' % (
                    bar['Name'], bar['SeatsCount']))
    else:
        print('%s имеет %s мест в зале. Это самый большой бар в списке.'
            % (result['Name'], result['SeatsCount']))


@load_data
def get_smallest_bar(sorted_by_seats):
    result = sorted_by_seats.pop(0)
    for bar in sorted_by_seats:
        if bar['SeatsCount'] == result['SeatsCount']:
            print('%s имеет %s мест в зале. '
                'Это один из самых маленьких баров в списке.' % (
                    bar['Name'], bar['SeatsCount']))
    else:
        print('%s имеет %s мест в зале. Это самый маленький бар в списке.'
            % (result['Name'], result['SeatsCount']))


@load_data
def get_closest_bar(sorted_by_seats ,longitude, latitude):
    my_coord = [[longitude, latitude]]
    list_of_coords = []
    for bar in sorted_by_seats:
        list_of_coords.append([(bar['geoData']['coordinates'][0]-my_coord[0][0]),(bar['geoData']['coordinates'][1]-my_coord[0][1])])
        list_of_coords.append(bar['Name'])
        list_of_coords.append(bar['Address'])
    print(list_of_coords)
    nearest_bar_coord = min(list_of_coords[::3])
    print(nearest_bar_coord)
    positiion_in_bar_coord_list = list_of_coords.index(nearest_bar_coord)
    print("Бар %s находится ближе всего к вам. Адрес: %s" % (list_of_coords.pop(positiion_in_bar_coord_list + 1), list_of_coords.pop(positiion_in_bar_coord_list + 1)))


if __name__ == '__main__':
    #select_action_to_do()
    #get_closest_bar('D:\\PyCharmPrj\\3_bars\\bars.json',37.464747458690351,55.784996653238541)
    N = int(input())
    lst = map(int, (input().split()))
    x = int(input())
    print(min(lst, key=lambda a: abs(a - x)))
