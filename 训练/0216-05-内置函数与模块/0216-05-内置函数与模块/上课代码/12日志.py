import logging

# 日志模块可以在开发的时候打印调试, 在服务器运行可以记录到文件
# 配置日志的级别
logging.basicConfig(level=logging.DEBUG)

logging.debug('这里是调试信息')
logging.info('这里是详情信息')
logging.warning('这里是警告信息')  # 默认情况下 警告以上的日志才会被打印出来
logging.error('这里是错误信息')
logging.critical('这里是危机信息')
