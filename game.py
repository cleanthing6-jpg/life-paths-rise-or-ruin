class Player:
    def __init__(self, name):
        self.name = name
        self.stats = {
            'health': 100,
            'wealth': 50,
            'morality': 50,
            'relationships': 50
        }

    def make_choice(self, choice):
        if choice == 'study':
            self.stats['wealth'] += 5
            self.stats['morality'] += 2
        elif choice == 'gamble':
            self.stats['wealth'] -= 10
            self.stats['morality'] -= 5
        elif choice == 'help_friend':
            self.stats['relationships'] += 10
            self.stats['morality'] += 5

    def show_stats(self):
        return self.stats

if __name__ == '__main__':
    p = Player('Hero')
    p.make_choice('study')
    print(p.show_stats())

