class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} атакует {other.name} на {self.attack_power} урона.")

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self, player_name):
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def start(self):
        print("Игра началась!")
        while self.player.is_alive() and self.computer.is_alive():
            # Ход игрока
            self.player.attack(self.computer)
            print(f"Здоровье {self.computer.name}: {self.computer.health}")
            if not self.computer.is_alive():
                print(f"{self.computer.name} мертв. {self.player.name} победил!")
                break

            # Ход компьютера
            self.computer.attack(self.player)
            print(f"Здоровье {self.player.name}: {self.player.health}")
            if not self.player.is_alive():
                print(f"{self.player.name} мертв. Компьютер победил!")
                break


# Пример использования
if __name__ == "__main__":
    game = Game("Бой (консоль)")
    game.start()
