import json

from myutils.LogWorker import LogMan


class AssertUtil():
    def __init__(self):
        self.log = LogMan(__name__)

    def assert_code(self, code, expected_code):
        try:

            assert int(code) == int(expected_code)
            self.log.info('pass!!!  code is {}, expected_code is {}'.format(code, expected_code))
            return True
        except:
            self.log.error('code error,code is {}, expected_code is {}'.format(code, expected_code))
            raise

    def assert_body(self, body, expected_body):
        '''

        :param body:
        :param expected_body:
        :return:
        '''
        try:
            assert body == expected_body
            self.log.error('pass!!!  body is {}, expected_body is {}'.format(body, expected_body))

            return True

        except:
            self.log.error('body error, body is {},expected_body is {}'.format(body, expected_body))
            raise

    def assert_in_body(self, body, expected_body):
        '''
        验证返回结果是否包含期望结果
        :param body:
        :param expected_body:
        :return:
        '''
        try:
            body = json.dumps(body)
            assert expected_body in body
            self.log.info('pass!!!  {} in {} '.format(expected_body, body))

            return True
        except:
            self.log.error('不具备包含关系(not in body) , body is {},expected_body is {}'.format(body, expected_body))
            raise
