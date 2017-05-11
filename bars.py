import json
import os


def load_data(filepath):
    if not os.path.exists(filepath):
        print('file not exist')
    with open(filepath, 'r', encoding='windows-1251') as file_handler:
        content_json = json.load(file_handler)
        # print(type(content_json))
        #print(content_json[1])
        for seats in content_json:
            print ('%s -> %s' %(seats['Name'], seats['SeatsCount']))


def get_biggest_bar(data):
    pass


def get_smallest_bar(data):
    pass


def get_closest_bar(data, longitude, latitude):
    pass


if __name__ == '__main__':
    pass

input_way = 'd:\pycharmprj\\3_bars\\bars.json'
load_data(input_way)
