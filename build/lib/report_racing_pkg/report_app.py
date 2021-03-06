from datetime import datetime, timedelta
import operator

start_file = 'start.log'
end_file = 'end.log'
abbreviations_file = 'abbreviations.txt'


def string_to_time(string):
    return datetime.strptime(string.rstrip()[14:], '%H:%M:%S.%f')


def build_report(path):
    result_dict = {}
    with open(f'..\\{path}\\{start_file}', 'r') as start:
        for line in start:
            result_dict[line[:3]] = string_to_time(line)
    with open(f'..\\{path}\\{end_file}', 'r') as end:
        for line in end:
            delta = string_to_time(line) - result_dict[line[:3]]
            if delta > timedelta(seconds=0):
                result_dict[line[:3]] = delta
            else:
                result_dict[line[:3]] = result_dict[line[:3]] - string_to_time(line)
    sorted_result_dict = sorted(result_dict.items(), key=operator.itemgetter(1))
    return sorted_result_dict, result_dict


def drivers_abbreviations(path):
    abbreviations_dict = {}
    driver_dict = {}
    sorted_result_dict, result_dict = build_report(path)
    with open(f'..\\{path}\\{abbreviations_file}', encoding='utf-8') as abbreviations:
        for line in abbreviations:
            line = line.rstrip().split('_')
            abbreviations_dict[line[0]] = [line[1], line[2]]
            driver_dict[line[1]] = [line[1], line[2], result_dict[line[0]]]
    return abbreviations_dict, driver_dict


def print_report(path, driver=None, order='asc'):
    sorted_result_dict, result_dict = build_report(path)
    abbreviations_dict, driver_dict = drivers_abbreviations(path)
    if driver is not None:
        print(driver_dict[driver][0], '  |', driver_dict[driver][1], '  |', str(driver_dict[driver][2])[3:11])
    else:
        if order == 'desc':
            sorted_result_dict = sorted_result_dict[::-1]
        number = 0
        for key in sorted_result_dict:
            number += 1
            print(number, abbreviations_dict[key[0]][0], '  |', abbreviations_dict[key[0]][1], '  |', str(key[1])[3:11])
            if number == 15:
                print(65 * '-')


if __name__ == '__main__':
    print_report('docs')
