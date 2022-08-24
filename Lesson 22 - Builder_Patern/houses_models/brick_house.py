from houses_models.abstact_house import AbstractHouse


class BrickHouse(AbstractHouse):

    def __init__(self, info: str):
        super().__init__('Цегляний будинок', info)