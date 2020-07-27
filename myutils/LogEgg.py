import logging
from config import conf
from config.conf import ConfigYaml

log_l = {
    'info': logging.INFO,
    'debug': logging.DEBUG,
    'warning': logging.WARNING,
    'error': logging.ERROR
}


class LogEgg(object):
    def __init__(self, log_file, log_name, log_level):
        self.log_file = log_file
        self.log_name = log_name
        self.log_level = log_level

        self.logger = logging.getLogger(self.log_name)
        self.logger.setLevel(log_l[self.log_level])

        if not self.logger.handlers:
            fh_stream = logging.StreamHandler()
            fh_stream.setLevel(self.log_level)
            formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s  %(message)s')
            fh_stream.setFormatter(formatter)

            fh_file = logging.FileHandler(self.log_file)
            fh_file.setLevel(log_l[self.log_level])
            fh_file.setFormatter(formatter)

            self.logger.addHandler(fh_stream)
            self.logger.addHandler(fh_file)


# 初始化
log_path = conf.get_log_path()
import datetime

current_time = datetime.datetime.now().strftime('%Y-%m-%d')
# 扩展名
log_ext = ConfigYaml().get_conf_log_extension()
import os

logfile = os.path.join(log_path, current_time + log_ext)
# print(logfile)
loglevel = ConfigYaml().get_conf_log()
# print(loglevel)



