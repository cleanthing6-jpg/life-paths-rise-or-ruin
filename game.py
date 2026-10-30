from city import City
from events import EventSystem
from npc import NPC
from storyline import Storyline
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
        self.storyline = Storyline()
        self.npcs = [NPC('Aria', 'scholar'), NPC('Darius', 'merchant')]

    def work(self, district, job):
        if job in self.city.available_jobs(district):
            self.stats['wealth'] += 10
            self.stats['morality'] += 1
        else:
            self.stats['health'] -= 5

    def live_day(self, day_number):
        print(f'--- Day {day_number} ---')
        self.work('Market', 'merchant')
        event, stats = self.events.trigger_event(self)
        print(f'Event: {event}')
        print('Stats:', stats)
        npc = random.choice(self.npcs)
        action = random.choice(['befriend', 'betray'])
        rel = npc.interact(self, action)
        print(f'Interaction with {npc.name} ({npc.role}): {action}, relationship = {rel}')
        destiny = self.storyline.check_destiny(self)
        print(destiny)

if __name__ == '__main__':
    p = Player('Hero')
    for day in range(1, 8):  # simulate a week
        p.live_day(day)

