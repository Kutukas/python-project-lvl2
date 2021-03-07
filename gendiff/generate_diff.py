import json


def generate_diff(file_path1, file_path2):
    dict1 = json_to_dict(file_path1)
    dict2 = json_to_dict(file_path2)
    raw_result = []
    for key in dict1:
        if key in dict2:
            temp_value1 = dict1[key]
            temp_value2 = dict2[key]
            if temp_value1 == temp_value2:
                raw_result.append((key, ' ', temp_value1))
            else:
                raw_result.append((key, '-', temp_value1))
                raw_result.append((key, '+', temp_value2))
        else:
            raw_result.append((key, '-', dict1[key]))
    for key in dict2:
        if key not in dict1:
            raw_result.append((key, '+', dict2[key]))
    sorted_raw_result = sorted(raw_result, key=lambda x: (x[0], -ord(x[1])))
    result = '\n{\n'
    for elem in sorted_raw_result:
        result += '  {} {}: {}\n'.format(elem[1], elem[0], elem[2])
    return result + '}' + '\n'


def json_to_dict(json_file_path):
    result = json.load(open(json_file_path))
    for key, value in result.items():
        if type(value) is bool:
            result[key] = str(value).lower()
    return result
