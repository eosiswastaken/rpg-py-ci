class Character:
    def __init__(self) -> None:
        self.__hp = 10

    def get_hp(self):
        return self.__hp

    def recieve_damage(self):
        self.__hp -= 1
        if self.__hp < 0:
            self.__hp = 0
