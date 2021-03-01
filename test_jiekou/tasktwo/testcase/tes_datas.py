import yaml
import os.path
# 公共模块
def get_datas():
    path = os.path.dirname(__file__) + "/task.yml"
    with open(path, encoding='utf-8') as f:
        datas = yaml.safe_load(f)
        # 获取文件中key为datas的数据
        read_datas = datas["read_members"]
        update_datas = datas['update_members']
        delete_datas = datas['delete_members']
        create_datas = datas['create_members']


        return [read_datas, update_datas,delete_datas,create_datas]


