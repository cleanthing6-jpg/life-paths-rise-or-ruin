class Storyline:
    def __init__(self):
        self.paths = {
            'greatness': {'condition': lambda stats: stats['wealth'] > 100 and stats['morality'] > 60},
            'ruin': {'condition': lambda stats: stats['health'] < 20 or stats['morality'] < 20},
            'obscurity': {'condition': lambda stats: stats['wealth'] < 50 and stats['relationships'] < 40}
        }

    def check_destiny(self, player):
        for path, data in self.paths.items():
            if data['condition'](player.stats):
                return f'Destiny path unlocked: {path}'
        return 'Destiny undecided...'

