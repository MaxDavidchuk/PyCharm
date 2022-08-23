from creators import *


class Client(object):

    def __init__(self, manager: LogisticManager):
        self._manager = manager

    def demo(self) -> None:
        self._manager.delivery_order()
