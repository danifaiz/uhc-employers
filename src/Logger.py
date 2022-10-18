import logging
import time
import logging.handlers

class Logger(object):
    def __init__(self):
        self.LOG_FILENAME = "Logs/" + time.strftime("job-%Y-%m-%d.log")
        self.DEBUG_FILENAME = "Logs/" + time.strftime("debug-%Y-%m-%d.log")
        self.dateTimeFormat = "%Y-%m-%d %H:%M:%S %p %Z"
    def writeLogs(self,message,logType="info"):
        if logType == "info":
            logging.basicConfig(level=logging.INFO,format = '%(asctime)s  %(levelname)-10s %(processName)s  %(name)s %(message)s', datefmt = self.dateTimeFormat,handlers=[logging.StreamHandler()])
            logging.Formatter.converter = time.gmtime
            logging.info(message)
        elif logType == "warning":
            logging.basicConfig(level=logging.WARNING,format = '%(asctime)s  %(levelname)-10s %(processName)s  %(name)s %(message)s', datefmt = self.dateTimeFormat,handlers=[logging.StreamHandler()])
            logging.warning(message)
        elif logType == "error":
            logging.basicConfig(level=logging.ERROR,format = '%(asctime)s  %(levelname)-10s %(processName)s  %(name)s %(message)s', datefmt = self.dateTimeFormat,handlers=[logging.StreamHandler()])
            logging.error(message)
        elif logType == "exception":
            logging.basicConfig(level=logging.ERROR,format = '%(asctime)s  %(levelname)-10s %(processName)s  %(name)s %(message)s', datefmt = self.dateTimeFormat,handlers=[logging.FileHandler(self.DEBUG_FILENAME),logging.StreamHandler()])
            logging.error(message,exc_info=True)
        else:
            pass
