import os
import inspect


class Common(object):
    def __init__(self):
        pass

    def log(self, msg):
        print(msg)

    def get_resource_path(self, filename):
        # Look for resources directory relative to python file
        prefix = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))), 'share')
        path = os.path.join(prefix, filename)
        self.log(path)
        return path
