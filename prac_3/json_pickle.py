import json
import pickle


def to_json_string(obj):
    print(json.dumps(obj))


def to_pickle_file(obj, filename):
    if not filename.endswith('.json'):
        filename += '.pickle'
    with open(filename, 'wb') as pickle_file:
        pickle.dump(obj, pickle_file)


def to_json_file(obj, filename: str, indent=4):
    if not filename.endswith('.json'):
        # todo аргумент, чтобы записать в одну строку
        filename += '.json'
    with open(filename, 'w') as f:
        json.dump(obj, f, indent=indent)


if __name__ == '__main__':
    dict_json = {
        1: 1,
        "2": 5,
        "str": [122, 0x123, 123],
        "tuple": (1, 2, 3),
        "d": {1: 5},
    }

    # to_json_string(dict_json)
    to_json_file(dict_json, 'dump_tmp.json')
