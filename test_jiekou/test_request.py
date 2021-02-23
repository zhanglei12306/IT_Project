import requests
from jsonpath import jsonpath
'''
get  ---> params
post  ---> data
'''
class TestRequests:
    def test_requ(self):
        r = requests.get('https://httpbin.testing-studio.com/get')
        print(r.status_code)
        print(r.text)
        print(r.json)
        assert r.status_code == 200

    def test_query(self):
        payload = {
            'level': 1,
            'name': 'zhenni'
        }
        r = requests.get('https://httpbin.testing-studio.com/get', params=payload)
        print(r.status_code)
        print(r.text)
        print(r.json)
        assert r.status_code == 200

    def test_post_form(self):
        payload = {
            'name': 'zhenni',
            'password': 'asdf'
        }
        r = requests.post('https://httpbin.testing-studio.com/post', data=payload)
        # print(r.status_code)
        print(r.text)
        # print(r.json)
        assert r.status_code == 200

    def test_heads(self):
        head = {
            'name': 'zhenni',
            'password': 'asdf'
        }
        r = requests.post('https://httpbin.testing-studio.com/post', headers=head)
        # print(r.status_code)
        print(r.text)
        # print(r.json)
        # assert r.status_code == 200
        assert r.json()['headers']['Password'] == "asdf"

    def test_post_json(self):
        payload = {
            'name': 'zhenni',
            'password': 1
        }
        r = requests.post('https://httpbin.testing-studio.com/post', json=payload)
        # print(r.status_code)
        print(r.text)
        # print(r.json)
        assert r.json()['json']['password'] == 1

    def test_json(self):
        payload = {
            'name': 'zhenni',
            'password': 1
        }
        r = requests.post('https://home.testing-studio.com/categories.json')
        # print(r.status_code)
        print(r.text)
        # print(r.json)
        assert r.json()['category_list']['categories'][0]['name'] == '开源项目'

    def test_jsonpath(self):
        payload = {
            'name': 'zhenni',
            'password': 1
        }
        r = requests.post('https://home.testing-studio.com/categories.json')
        # print(r.status_code)
        print(jsonpath(r.json(), '$..name'))
        # print(r.json)
        assert jsonpath(r.json(), '$..name')[0] == '开源项目'


    def test_cookeies(self):
        url = 'https://httpbin.testing-studio.com/cookies'
        # head = {
        #     'Cookie': 'ceshi',
        #     'User-Agent': 'python-requests'
        # }
        # r = requests.get(url= url, headers=head)
        # print(r.request.headers)
        head = {

            'User-Agent': 'python-requests'
        }
        cookies_data = {'ookie': 'ceshi',
                        'kie': 'ces'
                        }
        r = requests.get(url= url, headers=head, cookies=cookies_data )
        print(r.request.headers)
