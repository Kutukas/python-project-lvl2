import os
import json
import yaml


def get_correct_format(dict_data):
    for key, value in dict_data.items():
        if type(value) is bool:
            dict_data[key] = str(value).lower()
    return dict_data


def json_to_dict(json_file_path):
    result = json.load(open(json_file_path))
    return get_correct_format(result)


def yml_to_dict(yml_file_path):
    result = yaml.safe_load(open(yml_file_path))
    return get_correct_format(result)


def get_type(file_path):
    return os.path.splitext(file_path)[1]


def extract_data(file_path):
    if get_type(file_path) == '.json':
        return json_to_dict(file_path)
    elif get_type(file_path) == '.yml':
        return yml_to_dict(file_path)
