from Connector import Connection
from snew.Generator import Hasher
hasher = Hasher()
conn = Connection("18.216.32.253", "root", "password", "test")

def submit_info(username, password):
    """
    submit_info("'David'", 'Duan')
    submit_info("'David'", 'x')
    submit_info("'fail'", 'fail')

    Performs log in function.
    submit username and password to the server.
    """
    hashed = repr(hasher.hash(username[1:-1], password))
    
    try: 
        pw = conn.query('Login', ["hashedpw"], ['''username='''+username])
        print(pw[0][0])
        print(hashed)
        if (repr(pw[0][0]) == hashed):
            print("Log in success!")
        else:
            print("Invalid combination.")
    
    except Exception as e:
        # pop-up 
        print(e)
        print("Does not exist")


submit_info("'David'", "'PWDavid'")
submit_info("'David'", "'Wrong'")

conn.debugging()

