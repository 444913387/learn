# coding=utf-8

import json
import os
import sys

import curlify
import requests

from myutils.LogWorker import LogMan

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

CASE_DATA_PATH = './data/'

class GetDictParam():
    """
        这是一个解析dict 参数的类
        可以用于多参数的指定key 、 指定key集合解析key
    """

    @classmethod
    def get_value(cls, my_dict: dict, key: str):
        """
            这是一个递归函数
        """
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

    @classmethod
    def list_for_key_to_dict(cls, *args: tuple, my_dict: dict) -> dict:
        """
            接收需要解析的dict和 需要包含需要解析my_dict的keys的list
        :param my_dict: 需要解析的字典
        :param args: 包含需要解析的key的多个字符串
            # list_for_key_to_dict("code", "pageNo", "goodsId", my_dict=dict)
        :return: 一个解析后重新拼装的dict
        """
        result = {}
        if len(args) > 0:
            for key in args:
                result.update({key: cls.get_value(my_dict, key)})
        return result


from myutils.AssertUtil import AssertUtil


class HttpSender(GetDictParam):
    # ca_dir = '/Users/torsen/PycharmProjects/IHT/lib/ca.pem'
    session = requests.Session()
    assert_util = AssertUtil()
    log = LogMan(__name__)
    # session.verify = ca_dir


    @classmethod
    def generateCase(cls):
        rootdir = CASE_DATA_PATH
        listinfo = os.listdir(rootdir)
        # print(list)
        case_name = []
        url = []
        method = []
        params = []
        data = []
        headers = []
        assert_type = []
        assert_text = []
        case_desc = []
        for i in listinfo:
            if not i.startswith('__') and not i.startswith('#'):
                # print(i)

                with open(CASE_DATA_PATH + str(i), encoding='utf-8') as f:
                    datax = json.loads(f.read())
                    # print(datax, type(datax))
                    for i in datax:
                        case_name.append(i['case_name'])
                        url.append(i.get('url', {}))
                        method.append(i.get('method', {}))
                        params.append(i.get('params', {}))
                        data.append(i.get('data', {}))
                        headers.append(i.get('headers', {}))
                        assert_type.append(i.get('assert_type', {}))
                        assert_text.append(i.get('assert_text', {}))
                        case_desc.append(i.get('case_desc', {}))

        list_parameters = list(zip(case_name, url, method, params, data, headers, assert_type, assert_text, case_desc))
        return list_parameters


    def print_request(kwargs):
        print('{} {}'.format('curl输出：\n', curlify.to_curl(kwargs) + ' -v'))

    @staticmethod
    def print_curl(kwargs):
        print('{} {}'.format('curl输出：\n', curlify.to_curl(kwargs) + ' -v'))

    @staticmethod
    def return_curl(kwargs):
        return ('{}'.format(curlify.to_curl(kwargs) + ' -v'))

    @classmethod
    def print_resjson_statuscode(self, res):
        print(res.json())
        print(res.status_code)

    def send_http_request(self, url, method, **kwargs):
        return self.session.request(method, url, **kwargs)

    @classmethod
    def get(cls, url, **kwargs):
        return cls.session.get(url, **kwargs)

    @classmethod
    def post(cls, url, data, **kwargs):
        return cls.session.request('post', url, data=data, **kwargs)

    @classmethod
    def put(cls, url, data, **args):
        return cls.session.request('put', url, data=data, **args)

    @classmethod
    def patch(cls, url, data, **args):
        return cls.session.request('patch', url, data=data, **args)

    @classmethod
    def delete(cls, url, **kwargs):
        # print(
        #     '{} {}'.format('curl输出：\n', curlify.to_curl(cls.session.delete(url, **kwargs).request) + ' -v' + '\n\n'))
        return cls.session.request('delete', url, **kwargs)
