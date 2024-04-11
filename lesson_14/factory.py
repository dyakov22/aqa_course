from abc import ABC, abstractmethod


class Logger(ABC):

    @abstractmethod
    def write_log(self):
        pass


class ConsoleLogger(Logger):

    def write_log(self):
        print('Log was added to console')


class FileLogger(Logger):

    def write_log(self):
        print('Log was added to the file')


def factory_logger(target: str) -> Logger:
    """

    :param target: file, console
    :return: Logger()
    """
    if target == 'file':
        return FileLogger()
    elif target == 'console':
        return ConsoleLogger()
    else:
        raise AttributeError(f'This target is unknown {target}')




logger = factory_logger('file')
logger.write_log()

logger = factory_logger('console')
logger.write_log()




