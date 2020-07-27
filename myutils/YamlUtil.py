# 初始化创建一个类
# 初始化 文件是否存在 存在就读取 不存在就提示不存在

import os, yaml


class YamlReader:
    def __init__(self, ym):
        if os.path.exists(ym):
            self.ym = ym
        else:
            raise FileNotFoundError('文件不存在')
        self._data = None
        self._datas = None

    # 读取单个yaml文件
    def data(self):
        if not self._data:
            with open(self.ym, 'rb') as f:
                self._data = yaml.safe_load(f)
        return self._data

    # 读取多个
    def data_all(self):
        if not self._datas:
            with open(self.ym, 'rb') as f:
                self._datas = list(yaml.safe_load_all(f))
        return self._datas


