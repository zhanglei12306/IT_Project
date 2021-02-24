from test_jiekou.test_base64 import ApiRequests


class TestRequests(ApiRequests):
    req_data = {
        'method':'get',
        'url':'http://127.0.0.1:9999/demo.txt',
        'headers':None,
        'encoding':'base64'
    }

    def test_encod(self):
        ar = ApiRequests()
        print(ar.send(self.req_data))