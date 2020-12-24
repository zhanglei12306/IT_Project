import yaml

def get_datas():
    with open("./task.yml") as f:
        datas = yaml.safe_load(f)
        # 获取文件中key为datas的数据
        add_datas = datas["datas"]
        sub_datas = datas["sub"]
        mul_datas = datas["mul"]
        div_datas = datas["div"]
        # 获取文件中key为myids的数据
        add_ids = datas["myids"]
        return [add_datas, sub_datas, mul_datas, div_datas, add_ids]

