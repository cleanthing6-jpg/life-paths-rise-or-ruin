from city import City
from events import EventSystem
import random

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
        self.events = EventSystem()

    def work(self, district, job):
        if job in self.city.available_jobs(district):
            self.stats['wealth'] += 10
            self.stats['morality'] += 1
        else:
            self.stats['health'] -= 5

    def live_day(self):
        # Player works, then faces a random event
        self.work('Market', 'merchant')
        event, stats = self.events.trigger_event(self)
        print(f'Event: {event}')
        print('Stats:', stats)

if __name__ == '__main__':
    p = Player('Hero')
    p.live_day()

