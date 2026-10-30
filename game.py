from city import City

class Player:
    def __init__(self, name):
        self.name = name
        self.stats = {
            'health': 100,
            'wealth': 50,
            'morality': 50,
            'relationships': 50
        }
        self.city = City()

    def work(self, district, job):
        if job in self.city.available_jobs(district):
            self.stats['wealth'] += 10
            self.stats['morality'] += 1
        else:
            self.stats['health'] -= 5

    def show_stats(self):
        return self.stats

if __name__ == '__main__':
    p = Player('Hero')
    p.work('Market', 'merchant')
    print(p.show_stats())

