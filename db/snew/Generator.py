import bcrypt

class Hasher:
    def __init__(self, desired_key_bytes=16, rounds=300):
        self.desired_key_bytes = desired_key_bytes
        self.rounds = rounds

    def hash(self, username, password):
        key = bcrypt.kdf(password=password.encode(),
                         salt=username.encode(),
                         desired_key_bytes=self.desired_key_bytes,
                         rounds=self.rounds)

        return key


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
        return bcrypt.gensalt(self.work_rate, b'2a')

