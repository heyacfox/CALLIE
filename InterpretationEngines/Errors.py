class NotInMemoryError(Exception):
    def __init__(self, IDOfError):
        self.idError = IDOfError

class OutOfMemoryError(Exception):
    def __init__(self):
        self.myerror = "Ran out of memory"
