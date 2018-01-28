from Connector import Connection
from snew.Generator import Hasher
hasher = Hasher()
conn = Connection("18.216.32.253", "root", "password", "test")

def create_new(username, password):
    rows = ["username", "hashedpw"]
    hashed = hasher.hash(username[1:-1], password)
    values = ['{}'.format(username), hashed]
    try: 
        conn.insert("Login", rows, values)
    except Exception as e:
        # pop-up
        # try again
        print(e)

"""
rows = ["username", "hashedpw"]
values = ["'David'", "'Duan'"]
conn.insert("Login", rows, values)
"""

create_new("'David'", "'PWDavid'")
create_new("'Felix'", "'PWFelix'")
create_new("'Emily'", "'PWEmily'")
create_new("'Teresa'", "'PWTeresa'")

conn.debugging()
conn.delete("Login")
