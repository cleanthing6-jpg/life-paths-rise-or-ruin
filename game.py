from city import City
from events import EventSystem
from npc import NPC
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
        self.npcs = [NPC('Aria', 'scholar'), NPC('Darius', 'merchant')]

    def work(self, district, job):
        if job in self.city.available_jobs(district):
            self.stats['wealth'] += 10
            self.stats['morality'] += 1
        else:
            self.stats['health'] -= 5

    def live_day(self):
        # Work
        self.work('Market', 'merchant')
        # Random event
        event, stats = self.events.trigger_event(self)
        print(f'Event: {event}')
        print('Stats:', stats)
        # NPC interaction
        npc = random.choice(self.npcs)
        action = random.choice(['befriend', 'betray'])
        rel = npc.interact(self, action)
        print(f'Interaction with {npc.name} ({npc.role}): {action}, relationship = {rel}')

if __name__ == '__main__':
    p = Player('Hero')
    p.live_day()

