import json
import os


def load_data(func):
    def wrapped(filepath):
        if not os.path.exists(filepath):
            print('file not exist')
        with open(filepath, 'r', encoding='windows-1251') as file_handler:
            content_json = json.load(file_handler)
            sorted_by_seats = sorted(content_json,
                                     key=lambda seats: seats['SeatsCount'])
            func(sorted_by_seats)

    return wrapped


@load_data
def get_biggest_bar(sorted_by_seats):
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
def get_closest_bar(sorted_by_seats):  # , longitude, latitude):
    my_coord=[[37, 53]]
    list_of_coords=[]
    for bar in sorted_by_seats:
        #list_of_coords.append(my_coord-bar['geoData']['coordinates'])
        #value=my_coord[0][0]-bar['geoData']['coordinates'][0],my_coord[0][1]-bar['geoData']['coordinates'][1]
        #list_of_coords.update({bar['Name']:value})
        list_of_coords.append([(my_coord[0][0] - bar['geoData']['coordinates'][0]),(my_coord[0][1] - bar['geoData']['coordinates'][1])])
        list_of_coords.append(bar['Name'])
        #for small_a,small_b in list_of_coords
        #    print(min(small_a, small_b))
        #list_of_coords.append([bar['geoData']['coordinates'][0], bar['geoData']['coordinates'][1]])
        #for bar in list_of_coords:
        #    print(bar[1],bar[2])
    #for bars in list_of_coords:
    #    for bar in bars[1:3]:
    #        print(bar)
    print(list_of_coords)
    s=min(list_of_coords[::2])
    print(s)
    print(list_of_coords.index(s))
    print(list_of_coords.pop(205))



if __name__ == '__main__':
    pass

input_way = 'D:\prj\\3_bars\\bars.json'
#get_biggest_bar(input_way)
#get_smallest_bar(input_way)
get_closest_bar(input_way)
