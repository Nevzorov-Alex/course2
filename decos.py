"""
file support decorfator
"""
import sys
import logs.server_log_config
import  logs.client_log_config
import logging

# method define  module and define function
print('sys.argv=',sys.argv[0])
if sys.argv[0].find('client') == -1:
    logger = logging.getLogger('server')
else:
    logger = logging.getLogger('client')

def log(func_to_log):
    def log_saver(*args,**kwargs):
        ret = func_to_log(*args, **kwargs)
        logger.debug(f' was called function {func_to_log.__name__} with parameter {args},{kwargs}.'
                     f' from module {func_to_log.__module__}')
        return ret
    return log_saver
