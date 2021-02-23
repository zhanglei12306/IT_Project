from mitmproxy import http

class Counter:

    # def request(self, flow: http.HTTPFlow):
    #
    #     if 'baidu' in flow.request.pretty_url:
    #         flow.response = http.HTTPResponse.make(
    #             200,  # (optional) status code
    #             b"Hello World",  # (optional) content
    #             {"Content-Type": "text/html"}  # (optional) headers
    #         )

    def request(self, flow: http.HTTPFlow):

        if f'v5/stock/batch/quote.json' in flow.request.pretty_url:
            with open(r"C:\Users\10445\Desktop\tmp.json", "r", encoding="utf-8") as f:
                flow.response = http.HTTPResponse.make(
                    200,  # (optional) status code
                    f.read(),  # (optional) content
                    {"Content-Type": "application/json"}  # (optional) headers
                )

addons = [
    Counter()
]

