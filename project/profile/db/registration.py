from .Connector import Connection
from .snew.Generator import Hasher
hasher = Hasher()
conn = Connection("18.216.32.253", "root", "password", "test")

def new_user(username, password):
    """
    Register a new account with a username and password
    Submit username and password to the server. 
    The server checks if the username has been used already.
    If true, the user will be asked to re-enter the username.
    If false, the user is created successfully.

    Remark.
    create_new("'David'", "'PWDavid'")
    """
    rows = ["username", "hashedpw"]
    hashed = hasher.hash(password)
    values = ["'{}'".format(username), "{}".format(hashed)]
    return(conn.insert("Login", rows, values))


