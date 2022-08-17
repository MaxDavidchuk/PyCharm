from lib.managers.text_file_manager import TextFileManager
from lib.managers.json_file_manager import JsonFileManager
from lib.managers.binary_file_manager import BinaryFileManager


class UniversalFileManager(TextFileManager, JsonFileManager, BinaryFileManager):
    pass
