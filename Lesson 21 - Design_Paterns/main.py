from client import *
from creators import *


if __name__ == '__main__':

    client1 = Client(RoadLogisticManager('Kyiv', 'Lviv', 2, 'TOV PromInvest'))
    client2 = Client(SeeLogisticManager('Dnipro', 'Odesa', 4, 'TOV SeaLogicTrans'))
    client3 = Client(AirLogisticManager('Lviv', 'Kharkiv', 1, 'Svotoch LLC'))

    clients = [client1, client2, client3]
    for client in clients:
        client.demo()
