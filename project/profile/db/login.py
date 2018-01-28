from Connector import Connection
from snew.Generator import Hasher
hasher = Hasher()
conn = Connection("18.216.32.253", "root", "password", "test")

def login(username, password):
    """
    Performs log in function.
    Submit username and password to the server. 
    The server compares the password with the stored one.
    If true, login.status = success.
    If false, website gives a pop-up and the input form is cleared.
    """
    # compute the hash value for the given password.
    hashed = hasher.hash(password)
    try: 
        # extract the stored hash value from the database.
        pw = repr(conn.query('Login', ["hashedpw"], ['''username='''+username])[0][0])

        if (pw == hashed):
            print("Log in success!")
        else:
            print("Invalid combination.")
    
    except Exception as e:
        #!!!!!! pop-up !!!!!!
        print("""Fail - function = login
                 Possible reason: 
                 1. Username does not exist.
                 2. Password is incorrect.""")



