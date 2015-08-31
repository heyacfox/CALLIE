class NotInMemoryError(Exception):
    def __init__(self, id_of_error):
        self.id_error = id_of_error

class OutOfMemoryError(Exception):
    def __init__(self):
        self.my_error = "Ran out of memory"
