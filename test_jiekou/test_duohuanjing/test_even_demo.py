from test_jiekou.test_duohuanjing import evn_demo


class TestApi:
    data = {
        'method': 'get',
        'url': 'http://sss:9999/demo.txt',
        'headers': None
    }
    def test_send(self):
        api = evn_demo.Api()
        print(api.send(self.data).text)
