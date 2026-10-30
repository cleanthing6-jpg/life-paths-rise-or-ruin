class Player:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age
        self.stats = {
            'health': 100,
            'wealth': 50,
            'morality': 50,
            'relationships': 50
        }

    def live_day(self, day_number):
        print(f'--- Day {day_number} ---')
        self.age += 1/30
        if self.age >= 80:
            print(f"{self.name} has reached old age. Game Over.")
            return False
        return True

if __name__ == '__main__':
    p = Player('Hero')
    day = 1
    while p.live_day(day):
        day += 1
