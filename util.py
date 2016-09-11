import config
import inspect

def dprint(*msg):
    if config.DEBUG:
        frame = inspect.stack()[1]
        module = inspect.getmodule(frame[0])
        lineno = inspect.getlineno(frame[0])
        print('[{}:{}] {}'.format(module.__name__, lineno, ' '.join(map(str, msg))))
    else:
        print(' '.join(map(str, msg)))