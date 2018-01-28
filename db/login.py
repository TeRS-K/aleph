from Connector import Connection

conn = Connection("18.216.32.253", "root", "password", "test")

def submit_info(username, password):
    """
    submit_info("'David'", 'Duan')
    submit_info("'David'", 'x')
    submit_info("'fail'", 'fail')

    Performs log in function.
    submit username and password to the server.
    """
    input_info = [username, password]
    try: 
        pw = conn.query('Login', ["hashedpw"], ['''username=''' + input_info[0]])
        if (pw[0][0] == input_info[1]):
            print("Log in success!")
        else:
            print("Invalid combination.")
    
    except Exception as e:
        # pop-up
        print("Does not exist")






