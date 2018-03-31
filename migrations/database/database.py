from Connector import Connection
from snew.Generator import Hasher, Coder
from datetime import datetime, timedelta 
hasher = Hasher()
coder = Coder()
conn = Connection("18.216.32.253", "root", "password", "test")

def new_user(username, password):
    rows = ["username", "hashedpw"]
    hashed = hasher.hash(password)
    values = ['{}'.format(username), '{}'.format(hashed)]
    try: 
        conn.insert("Login", rows, values)
    except Exception as e:
        # pop-up and clear-form
        print(e)


def log_in(username, password):
    hashed = hasher.hash(password)
    try: 
        pw = repr(conn.query('Login', ["hashedpw"], ['''username='''+username])[0][0])
        if (pw == hashed):
            print("Log in success!", username)
        else:
            print("Invalid combination.")
    except Exception as e:
        print(e, username, password)


def name_to_id(username):
    try: 
        return(conn.query('Login', ["userID"], ['''username={}'''.format(username)])[0][0])
    except Exception as e:
        print(e)
        print("Fail : name_to_id.", username)
  

def id_to_name(userID):
    try: 
        return conn.query('Login', ["username"], ['''userID=''' + str(userID)])[0][0]
    except Exception as e:
        print(e)
        print("Fail : id_to_name.", userID)


def fetch_friend_status(username, friend_name):

    try:
        friend_id = name_to_id(friend_name)
        my_id = name_to_id(username)

        try:
            conn.query('Friends', ["friendID"], ['''userID=''' + str(my_id)])

            try:
                # Order by time updated in descending order, so it returns the latest location.
                status = conn.query('Status', ["status", "ts"], conditions=['''userID=''' + str(friend_id)], 
                                    order=["{}".format('ts'), "DESC"])[0]
                print("Status of {}: {}".format(friend_name, status))
                return status    

            except Exception as e:
                print(e)
                print("FAIL: Fail to return query status.", username, friend_name)

        except Exception as e:
            print(e)
            print("FAIL: You two are not friends.", username, friend_name)
    
    except Exception as e:
        print(e)
        print("FAIL: Either user does not exist.", username, friend_name)


def fetch_friend_location(username, friend_name):

    try:
        friend_id = name_to_id(friend_name)
        my_id = name_to_id(username)

        try:
            conn.query('Friends', ["friendID"], ['''userID=''' + str(my_id)])

            try:
                # Order by time updated in descending order, so it returns the latest location.
                location = conn.query('Location', ["location", "ts"], conditions=['''userID=''' + str(friend_id)], 
                                      order=["{}".format('ts'), "DESC"])[0]
                print("Location of {}: {}".format(friend_name, location))
                return location  

            except Exception as e:
                print(e)
                print("FAIL: Fail to return query location.", username, friend_name)

        except Exception as e:
            print(e)
            print("FAIL: You two are not friends.", username, friend_name)
    
    except Exception as e:
        print(e)
        print("FAIL: Either user does not exist.", username, friend_name)


def delete_account(username):
    my_id = name_to_id(username)
    conn.delete("Location", ['''userID={}'''.format(str(my_id))])
    conn.delete("Status", ['''userID={}'''.format(str(my_id))])
    conn.delete("AddCode", ['''userID={}'''.format(str(my_id))])
    conn.delete("Friends", ['''userID={}'''.format(str(my_id))])
    conn.delete("Friends", ['''friendID={}'''.format(str(my_id))])
    conn.delete("Frequency", ['''userID={}'''.format(str(my_id))])
    conn.delete("Login", ['''username={}'''.format(username)])


def delete_friend(username, friend_name):

    try:
        friend_id = name_to_id(friend_name)
        my_id = name_to_id(username)
        try:
            conn.query('Friends', ["friendID"], ['''userID=''' + str(my_id)])
            try:
                # confirmation: pop_up
                # confirmation = input()
                conn.delete("Friends", ['''userID=''' + str(my_id), '''friendID=''' + str(friend_id)])
                conn.delete("Friends", ['''userID=''' + str(friend_id), '''friendID=''' + str(my_id)])
  
            except Exception as e:
                print(e)
                print("FAIL: Fail to delete friends.", username, friend_name)

        except Exception as e:
            print(e)
            print("FAIL: You two are not friends.", username, friend_name)
    
    except Exception as e:
        print(e)
        print("FAIL: Either user does not exist.", username, friend_name)


def get_all_friends(username):
    try:
        my_id = name_to_id(username)

        try: 
            friend_list = conn.query('Friends', ["friendID"], ['''userID={}'''.format(str(my_id))])
            output = []
            for i in friend_list:
                output.append(i[0])
            return output # a list
        
        except Exception as e:
            print(e)
            print("FAIL: Fail to query all friends.", username)

    except Exception as e:
        print(e)
        print("FAIL: User does not exist.", username)


def auto_deletion():
    conn.delete("Location", ['''ts < (NOW() - INTERVAL 10 MINUTE)'''])
    conn.delete("AddCode", ['''ts < (NOW() - INTERVAL 10 MINUTE)'''])
    conn.delete("Status", ['''ts < (NOW() - INTERVAL 10 MINUTE)'''])


def add_friend(username, mycode):
    try: 
        my_id = name_to_id(username)    

        try: 
            friend_id = conn.query('AddCode', ["userID"], 
                    conditions=['''code={}'''.format(mycode)])[0][0]

            try: 
                rows = ["userID", "friendID"]
                values = ["{}".format(my_id), "{}".format(friend_id)]
                conn.insert("Friends", rows, values)

                rows = ["userID", "friendID"]
                values = ["{}".format(friend_id), "{}".format(my_id)]
                conn.insert("Friends", rows, values)

                conn.delete("AddCode", ['''userID={}'''.format(friend_id)])

            except Exception as e:
                print(e)
                print("FAIL: Fail to add friend", username, friend_id)

        except Exception as e:
            print(e)
            print("FAIL: Invalid AddCode.", username, mycode)

    except Exception as e:
        print(e)
        print("FAIL: User does not exist.", username, mycode)
    

def generate_code(username):
    try: 
        my_id = name_to_id(username)

        if conn.query('AddCode', columns=["userID"], conditions=['''userID={}'''.format(my_id)]):
            conn.delete('AddCode', ['''userID={}'''.format(my_id)])

        my_code = repr(coder.getCode(username))
        rows = ["userID", "code"]
        values = ["{}".format(my_id), "{}".format(my_code)]
        conn.insert("AddCode", rows, values)
        return my_code

    except Exception as e:
        print(e)
        print("FAIL: User does not exist.")


def update_location(username, location):
    try: 
        my_id = name_to_id(username)
        rows = ["userID", "location"]
        values = ["{}".format(str(my_id)), "{}".format(location)]
        conn.insert("Location", rows, values)
        try:
            if conn.query("Frequency", ["frequency"], ["userID={}".format(str(my_id)),
                                                       "location={}".format(location)]):
                conn.update("Frequency", ["frequency=frequency+1"], ["userID={}".format(str(my_id)),
                                                                        "location={}".format(location)])
            else:   
                 conn.insert("Frequency", ["userID", "location", "frequency"], 
                                          ["{}".format(str(my_id)), "{}".format(location), "1"])                                                         
        except Exception as e:
            print(e)

    except Exception as e:
        print(e)
        print("Fail: update_location")


def update_status(username, status):
    try: 
        my_id = name_to_id(username)
        rows = ["userID", "status"]
        values = ["{}".format(str(my_id)), "{}".format(status)]
        conn.insert("Status", rows, values)

    except Exception as e:
        print(e)
        print("Fail: update_status")


def fetch_status(username):
    try:
        my_id = name_to_id(username)
        status = conn.query('Status', ["status", "ts"], conditions=['''userID=''' + str(my_id)], 
                                    order=["{}".format('ts'), "DESC"])[0]
        return status
                                
    except Exception as e:
        print(e)
        print("Fail: fetch_my_status")


def fetch_location(username):
    try:
        my_id = name_to_id(username)
        location = conn.query('Location', ["location", "ts"], conditions=['''userID=''' + str(my_id)], 
                                    order=["{}".format('ts'), "DESC"])[0]
        return location
                                
    except Exception as e:
        print(e)
        print("Fail: fetch_my_status")







