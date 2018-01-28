import bcrypt
from Crypto.Hash import SHA3_512

class Hasher:
    def __init__(self):
        pass

    def hash(self, password):
        hash = SHA3_512.new()
        hash.update(password.encode())

        return hash.hexdigest()


class Coder:
    '''
    friend Code generator Class
    optional work_rate parameter proportional to run time
    '''
    def __init__(self, work_rate=12):
        '''
        :param work_rate: optional, proportional to run-time
        '''
        self.work_rate=work_rate

    def getCode(self, username):
        '''
        :param username: username of code giver
        :return: code in bits
        '''
        return str(bcrypt.gensalt(self.work_rate, b'2a'), 'latin-1')

