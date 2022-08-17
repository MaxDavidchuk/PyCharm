class MusicPlayerMixin(object):
    @staticmethod
    def play_music(song):
        print(f'Now playing: {song}')
# ===============================================


class Vehicle(object):
    pass


class Car(Vehicle, MusicPlayerMixin):
    @staticmethod
    def ride():
        print('Car is riding ...')


class Boat(MusicPlayerMixin):
    @staticmethod
    def swim():
        print('Boat is swimming')
# ===============================================


class Device(object):
    pass


class Smartphone(Device, MusicPlayerMixin):
    pass


class Radio(Device, MusicPlayerMixin):
    pass
