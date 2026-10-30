import random

class Player:
    def __init__(self, name, age=18, generation=1):
        self.name = name
        self.age = age
        self.generation = generation
        self.stats = {
            'health': 100,
            'wealth': 50,
            'morality': 50,
            'relationships': 50
        }
        self.children = []
        self.married = False

    def maybe_marry(self):
        if not self.married and 20 <= self.age <= 35 and self.stats['relationships'] >= 40:
            if random.random() < 0.1:  # 10% chance per day
                self.married = True
                print(f"{self.name} got married!")

    def maybe_have_child(self):
        if self.married and self.age >= 25 and len(self.children) < 3:
            if random.random() < 0.02:  # 2% chance per day
                child_name = f"{self.name}_Child{len(self.children)+1}"
                child = Player(child_name, age=0, generation=self.generation+1)
                child.stats['wealth'] = self.stats['wealth'] // 2
                child.stats['morality'] = self.stats['morality']
                self.children.append(child)
                print(f"{self.name} had a child: {child.name}")

    def live_day(self, day_number):
        print(f'--- Day {day_number} --- (Gen {self.generation}, Age {int(self.age)})')
        self.age += 1/30
        self.maybe_marry()
        self.maybe_have_child()
        if self.age >= 80 or self.stats['health'] <= 0:
            print(f"{self.name} has reached old age or died. Game Over for this generation.")
            return False
        return True

if __name__ == '__main__':
    p = Player('Hero')
    day = 1
    while True:
        if not p.live_day(day):
            if p.children:
                p = p.children[0]  # continue with first child
                print(f"New generation begins: {p.name}")
                day = 1
            else:
                print("No heirs. Game Over.")
                break
        day += 1
