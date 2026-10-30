class NPC:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.relationship = 50

    def interact(self, player, action):
        if action == 'befriend':
            self.relationship += 10
            player.stats['relationships'] += 5
        elif action == 'betray':
            self.relationship -= 15
            player.stats['morality'] -= 10
        return self.relationship

