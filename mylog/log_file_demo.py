# Format格式说明
# ➢%(levelno)s: 打印日志级别的数值
# ➢%(levelname)s:打印日志级别名称
# ➢%(pathname)s:打印当前执行程序的路径，其实就是sys.argv[0]
# ➢%(filename)s: 打印当前执行程序名
# ➢%(funcName)s: 打印日志的当前函数
# ➢%(lineno)d: 打印日志的当前行号
# ➢%(asctime)s: 打印日志的时间
# ➢%(thread)d:打印线程ID
# ➢%(threadName)s:打印线程名称
# ➢%(process)d: 打印进程ID
# ➢%(message)s:打印日志信息


import logging

logger = logging.getLogger('log_file_demo')

logger.setLevel(logging.INFO)
fh_stream = logging.StreamHandler()

fh_file = logging.FileHandler('./test.log')

fh_stream.setLevel(logging.INFO)
fh_file.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s  %(message)s')
fh_stream.setFormatter(formatter)

fh_file.setFormatter(formatter)

logger.addHandler(fh_stream)
logger.addHandler(fh_file)
logger.info('this is a info')
logger.debug('this is a debug')
