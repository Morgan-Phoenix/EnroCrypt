class ModifiedError(Exception):
    def __init__(self):
        self.msg = 'The List Provided To The Function Is Modified'
        super().__init__(self.msg)
        exit()
class ListIndexError(Exception):
    def __init__(self):
        self.msg = 'Returned List Must Only Have 4 Elements'
        super().__init__(self.msg)
        exit()
class NoKeyFile(Exception):
    def __init__(self):
        self.msg = 'No Path For The Key File was Provided'
        super().__init__(self.msg)
        exit()
class List(Exception):
    def __init__(self):
        self.msg = "Must Be A List"
        super().__init__(self.msg)
        exit()
class KeyError(Exception):
    def __init__(self,bits:int) -> None:
        self.bits = bits
        self.msg = f"Key Must Be Of 32, 24 or 16 bits not {self.bits} bits"
        super().__init__(self.msg)
        exit()