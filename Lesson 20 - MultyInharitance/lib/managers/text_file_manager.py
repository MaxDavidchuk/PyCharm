class TextFileManager(object):

    @staticmethod
    def write_text_to_file(file_path: str, text: str) -> None:
        with open(file_path, 'w') as file:
            file.write(text)
            print(f'Text save to file: {file_path}')

    @staticmethod
    def read_text_from_file(file_path: str) -> None:
        with open(file_path, 'r') as file:
            text = file.read()
            print(f'Text read from file: {file_path}')
            print(text)
