import requests


class Api:
    env = {
        'default': 'tes',
        'test_quehuan': {
            'dev': '127.0.0.1',
            'tes': '127.0.2.2'
        }

    }

    def send(self, data: dict):
        data['url'] = str(data['url']).replace('sss', self.env['test_quehuan'][self.env['default']])
        print(data['url'])
        re = requests.request(method=data['method'], url=data['url'], headers=data['headers'])
        return re