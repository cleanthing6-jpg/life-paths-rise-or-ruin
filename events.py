import random

class EventSystem:
    def __init__(self):
        self.events = [
            {'name': 'Festival', 'effect': {'morality': +5, 'relationships': +10}},
            {'name': 'Economic Crisis', 'effect': {'wealth': -15, 'morality': -5}},
            {'name': 'Street Fight', 'effect': {'health': -20, 'morality': -10}},
            {'name': 'Job Opportunity', 'effect': {'wealth': +20, 'relationships': +5}},
            {'name': 'Betrayal', 'effect': {'relationships': -15, 'morality': -10}}
        ]

    def trigger_event(self, player):
        event = random.choice(self.events)
        for stat, change in event['effect'].items():
            player.stats[stat] += change
        return event['name'], player.stats

