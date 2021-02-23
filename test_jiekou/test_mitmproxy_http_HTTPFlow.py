from mitmproxy import ctx
import mitmproxy.http

class Counter:
    def __init__(self):
        self.num = 0

    def request(self, flow: mitmproxy.http.HTTPFlow):
        self.num = self.num + 1
        ctx.log.info("We've seen %d flows" % self.num)
        ctx.log.info("Base contest %s" % str(flow.get_state()))

addons = [
    Counter()
]