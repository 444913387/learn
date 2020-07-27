# 获取基本目录，获取当前项目点 绝对路径
#
# 定义config目录的路径，定义config.yml 的文件路径
# 读取配置文件
import os
from myutils import YamlUtil

CURRENT = os.path.abspath(__file__)
# print(CURRENT)
BASE_DIR = os.path.dirname(os.path.dirname(CURRENT))
# print(BASE_DIR)
# C:\Users\Administrator\PycharmProjects\learn\config\conf.py
# C:\Users\Administrator\PycharmProjects\learn

# config路径
_config_path = BASE_DIR + os.sep + "config"

# conf.yml路径
_conf_file = _config_path + os.sep + 'conf.yml'


#log文件路径

_log_path =  _config_path + os.sep + 'logs'


def get_config_path():
    return _config_path


def get_config_file():
    return _conf_file

def get_log_path():
    return _log_path


class ConfigYaml(object):
    def __init__(self):
        self.config = YamlUtil.YamlReader(get_config_file()).data_all()

    @classmethod
    def get_value(cls, my_dict: dict, key: str):

        if isinstance(my_dict, dict):
            if my_dict.get(key) or my_dict.get(key) == 0 or my_dict.get(key) == '' \
                    and my_dict.get(key) is False or my_dict.get(key) == []:
                return my_dict.get(key)

            for my_dict_key in my_dict:
                if cls.get_value(my_dict.get(my_dict_key), key) or \
                        cls.get_value(my_dict.get(my_dict_key), key) is False:
                    return cls.get_value(my_dict.get(my_dict_key), key)

        if isinstance(my_dict, list):
            for my_dict_arr in my_dict:
                if cls.get_value(my_dict_arr, key) \
                        or cls.get_value(my_dict_arr, key) is False:
                    return cls.get_value(my_dict_arr, key)

    def get_conf_url(self):
        return self.get_value(self.config[0], 'url')


    def get_conf_log(self):
        return  self.get_value(self.config[0],'log_level')


    def get_conf_log_extension(self):
        return self.get_value(self.config[0],'log_extension')



if __name__ == '__main__':
    cf = ConfigYaml()
    print(cf.get_conf_log_extension())
