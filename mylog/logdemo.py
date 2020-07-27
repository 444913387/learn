

import logging

logging.basicConfig(level=logging.INFO,format='%(asctime)s-%(name)s-%(levelname)s-%(message)s')

logger = logging.getLogger('log_demo')

logger.info('info')
logger.debug('debug')
logger.warning('warning')

