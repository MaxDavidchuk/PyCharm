import json


class JsonFileManager(object):

    @staticmethod
    def write_dict_to_file(file_path: str, data: dict) -> None:
        with open(file_path, 'w') as file:
            json.dump(data, file)
            print(f'Dict save to file: {file_path}')

    @staticmethod
    def read_dict_from_file(file_path: str) -> None:
        with open(file_path, 'r') as file:
            data = json.load(file)
            print(f'Dict read from file: {file_path}')
            for key, value in data.items():
                print(f'{key} -> {value}')
