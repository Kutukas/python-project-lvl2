import os
import json
import yaml


def json_to_dict(json_file_path):
    result = json.load(open(json_file_path))
    for key, value in result.items():
        if type(value) is bool:
            result[key] = str(value).lower()
    return result


def yml_to_dict(yml_file_path):
    result = yaml.safe_load(open(yml_file_path))
    for key, value in result.items():
        if type(value) is bool:
            result[key] = str(value).lower()
    return result


def get_type(file_path):
    return os.path.splitext(file_path)[1]


def extract_data(file_path):
    if get_type(file_path) == '.json':
        return json_to_dict(file_path)
    elif get_type(file_path) == '.yml':
        return yml_to_dict(file_path)
