from houses_models.abstact_house import AbstractHouse


class StoneHouse(AbstractHouse):

    def __init__(self, info: str):
        super().__init__('Кам\'яний будинок', info)
