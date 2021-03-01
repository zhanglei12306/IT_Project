import yaml


def test_yaml1():
    env = yaml.safe_load(open('evn,yaml'))
    with open('evn,yaml', 'w') as f:
        yaml.safe_dump(data=env, stream=f)