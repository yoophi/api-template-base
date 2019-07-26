users = [
    {
        'name': 'user1',
        'password': 'secret',
        'created_at': '2019-01-01 00:00:00',
    },
    {
        'name': 'user2',
        'password': 'secret',
        'created_at': '2019-01-01 00:00:00',
    },
]


class MemRepo:
    def __init__(self, data):
        self.data = data

    def list(self, filters=None):
        result = [User.from_dict(d) for d in self.data]
        return result
