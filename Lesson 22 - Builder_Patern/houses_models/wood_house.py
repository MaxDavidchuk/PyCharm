from houses_models.abstact_house import AbstractHouse


class WoodHouse(AbstractHouse):

    def __init__(self, info: str):
        super().__init__('Дерев\'яний будинок', info)
