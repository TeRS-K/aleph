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

