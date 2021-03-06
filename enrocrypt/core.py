from enrocrypt.hashing import Hashing
from enrocrypt.encryption import Encryption
from enrocrypt.basic import Basic

class Core(Hashing,Encryption,Basic):
    '''Given Below Is The Syntax To Set Configurations For This Class. This Must Be Used As Is(Just Change The File Path)

    config = {
    'configs':{
        'salt_file':"The Path Of The File Where Your Salt Is Stored"
        }
    }'''
    def __init__(self) -> None:
        self.salt = ''
        self.byt = 512
    def set_config(self,con:dict):
        configs = (con['salt_file'])
        value = self.__Set_Salt(configs)
        return value
    def __str__(self) -> str:
        return "The Base Class Of EnroCrypt"
    def __Set_Salt(self,salt:list):
        try:
            with open(salt,'r') as f:
                salts = f.read()
            self.salt = bytes(salts.encode())
            return True
        except FileNotFoundError:
            return print(Warning("No Salt File Found At The Given Location Using Random Salt"))
        else:
            return False
    def get_hash_object(self):
        '''Returns A Hashing Class Object That Is Pre-Configured To Use Custom Salt If Any'''
        hashing = Hashing()
        if self.salt == "":
            print(print(Warning("No Personalized Salt Loaded In The Memory, Using Random Salt")))
        hashing(bytes(self.salt.encode()),self.byt)
        return hashing