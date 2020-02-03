class Error(Exception):
    def __init__(self, msg):
        self.message = msg

    def what(self):
        return self.message

class ConfFileError(Error):
    pass


