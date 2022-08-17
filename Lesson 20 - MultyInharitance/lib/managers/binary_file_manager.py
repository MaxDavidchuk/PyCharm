import pickle


class BinaryFileManager(object):

    @staticmethod
    def write_object_to_file(file_path: str, obj) -> None:
        with open(file_path, 'wb') as file:
            pickle.dump(obj, file)
            print(f'Object save to file: {file_path}')

    @staticmethod
    def read_object_from_file(file_path: str) -> None:
        with open(file_path, 'rb') as file:
            obj = pickle.load(file)
            print(f'Object read from file: {file_path}')
            print(obj)
