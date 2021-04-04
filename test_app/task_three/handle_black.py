import yaml
from appium.webdriver.common.mobileby import MobileBy
def handle_black(fun):
    def run(*args, **kwargs):
        self = args[0]
        with open("../black_list.yml", "r", encoding="utf-8") as f:
            black_list = yaml.load(f)
            print(black_list)
        try:
            return fun(*args, **kwargs)
        except Exception as e:
            for balck in black_list:
                # print(balck)
                eles = self.driver.find_elements(*balck)

                if len(eles) > 0:
                    eles[0].click()
                    return fun(*args, **kwargs)
            raise e
    return run