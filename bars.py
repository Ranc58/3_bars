import json


def load_data(func):
    def wrapped(filepath):
        try:
            file_handler = open(filepath, 'r', encoding='windows-1251')
            content_json = json.load(file_handler)
            func(content_json)
            file_handler.close()
        except ValueError:
            print('JSON file contain errors! ')
        except FileNotFoundError:
            print('Not found JSON file. Please check way. ')
    return wrapped


@load_data
def get_biggest_bar(content_json):
    sorted_by_seats = sorted(content_json,
                             key=lambda seats: seats['SeatsCount'])
    result = sorted_by_seats.pop()
    for bar in sorted_by_seats:
        # print(bar['geoData']['coordinates'])  # TODO Удалить!
        if bar['SeatsCount'] == result['SeatsCount']:
            print('%s имеет %s мест в зале. '
                  'Это один из самых больших баров в списке.' % (
                      bar['Name'], bar['SeatsCount']))
    else:
        print('%s имеет %s мест в зале. Это самый большой бар в списке.'
              % (result['Name'], result['SeatsCount']))


@load_data
def get_smallest_bar(content_json):
    sorted_by_seats = sorted(content_json,
                             key=lambda seats: seats['SeatsCount'])
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
def get_closest_bar(content_json):  # , longitude, latitude):
    my_coord = [38, 57]
    list_of_coords = []
    sorted_by_seats = sorted(content_json,
                             key=lambda seats: seats['SeatsCount'])
    for bar in sorted_by_seats:
        # list_of_coords.append(my_coord-bar['geoData']  TODO Удалить!
        #                       ['coordinates'])         TODO Удалить!
        list_of_coords.append([(my_coord[0] -
                                bar['geoData']['coordinates'][0]),
                               (my_coord[1] -
                                bar['geoData']['coordinates'][1])])
    print(sorted(list_of_coords))


if __name__ == '__main__':
    input_way = 'D:\Pycharmprj\\3_bars\\bars.json'
    # get_biggest_bar(input_way)
    # get_smallest_bar(input_way)
    get_closest_bar(input_way)
