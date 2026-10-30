class City:
    def __init__(self):
        self.districts = {
            'Market': ['merchant', 'trader'],
            'University': ['scholar', 'teacher'],
            'Arena': ['warrior', 'performer'],
            'Temple': ['mystic', 'healer'],
            'TechHub': ['engineer', 'developer']
        }

    def available_jobs(self, district):
        return self.districts.get(district, [])

if __name__ == '__main__':
    city = City()
    print('Jobs in Market:', city.available_jobs('Market'))

