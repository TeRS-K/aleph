from Connector import Connection
from snew.Generator import Hasher, Coder
from datetime import datetime, timedelta 
from login import login
from registration import new_user

hasher = Hasher()
coder = Coder()
conn = Connection("18.216.32.253", "root", "password", "test")

def name_to_id(username):
    try: 
        return(conn.query('Login', ["userID"], ['''username={}'''.format(username)])[0][0])
    except:
        print("Fail : name_to_id.")
  
def id_to_name(userID):
    try: 
        my_name = conn.query('Login', ["username"], ['''userID=''' + str(userID)])[0][0]
        return my_name
    except:
        print("Fail : id_to_name.")

def fetch_friend_status(username, friend):
    """
    username: your name
    friend: your friend's name
    return your friend's status as a string.
    """
    try:
        # SELECT <userID> FROM Login WHERE username = <friend_id>
        # This step checks if your friend exists.
        friend_id = name_to_id(friend)
        my_id = name_to_id(username)

        try:
            # SELECT <userID> FROM Friends WHERE friendID = <friend_id>
            # This step checks if you are friends with your friend.
            # This list contains every location your friend has been to.
            friendlist = conn.query('Friends', ["friendID"], ['''userID=''' + str(my_id)])

            try:
                # Rrder by time updated in descending order, so it returns the latest location.
                status = conn.query('Status', ["status", "ts"], conditions=['''userID=''' + str(friend_id)], 
                                    order=["{}".format('ts'), "DESC"])[0]
                print("Get friend's status successfully.")
                print(status) ## status, time
                return status    
            except Exception as e:
                print("Failed last step of fetch_friend_status")
                print(e)

        except Exception as e:
            print("Fail: fetch_friend_status - You two are not friends.")
    
    except:
        print("Friend does not exist.")
    
def fetch_friend_location(username, friend):
    """
    username: your name
    friend: your friend's name
    return your friend's location as a string.
    """
    try:
        # SELECT <userID> FROM Login WHERE username = <friend_id>
        # This step checks if your friend exists.
        friend_id = name_to_id(friend)
        my_id = name_to_id(username)

        try:
            # SELECT <userID> FROM Friends WHERE friendID = <friend_id>
            # This step checks if you are friends with your friend.
            # This list contains every location your friend has been to.
            friendlist = conn.query('Friends', ["friendID"], ['''userID=''' + str(my_id)])

            try:
                # Rrder by time updated in descending order, so it returns the latest location.
                location = conn.query('Location', ["location", "ts"], conditions=['''userID=''' + str(friend_id)], 
                                      order=["{}".format('ts'), "DESC"])[0]
                print("Get friend's location successfully.")
                print(location) ## location, time
                return location    
            except Exception as e:
                print("Failed last step of fetch_friend_location")
                print(e)

        except Exception as e:
            print("Fail: fetch_friend_status - You two are not friends.")
    
    except:
        print("Friend does not exist.")
    
def delete_account(username):
    """
    requires pop_up for confirmation.
    "This process is invertible; type the following statement to proceed...""
    This deletes the current account.
    """
    confirmation = input()
    if (confirmation == "Y"):
        conn.delete("Login", ['''username={}'''.format(username)])
    
    # check if other table has updated as well.

def delete_friend(username, friend):
    """
    username: your username
    friend: friend's username you want to delete
    delete this friend
    """
    try:
        friend_id = name_to_id(friend)
        my_id = name_to_id(username)
        try:
            # print(conn.query('Friends', ["friendID"], ['''userID=''' + str(my_id)]))
            is_friend = conn.query('Friends', ["friendID"], ['''userID=''' + str(my_id)])
            try:
                # confirmation: pop_up
                # confirmation = input()
                conn.delete("Friends", ['''userID=''' + str(my_id), '''friendID=''' + str(friend_id)])
                print("removed.")
  
            except Exception as e:
                print(e)
                print("fail") 

        except Exception as e:
            print(e)
            print("You two are not friends.")
    
    except Exception as e:
        print(e)
        print("Friend does not exist.")

def get_all_friends(username):
    try:
        my_id = name_to_id(username)
        friend_list = conn.query('Friends', ["friendID"], ['''userID={}'''.format(str(my_id))])
        output = []
        for i in friend_list:
            output.append(i[0])
        print(output)
    except:
        print("Fail: get_all_friends")

def update_location(username, location):
    """
    Given username and location, update location.
    """
    try: 
        my_id = name_to_id(username)
        rows = ["userID", "location"]
        values = ["{}".format(str(my_id)), 
                  "{}".format(location)]
        conn.insert("Location", rows, values)
        print("Done: update_location")
    except Exception as e:
        print(e)
        print("Fail: update_location")

def update_status(username, status):
    """
    Given username and status (integer value), update status.
    """
    try: 
        my_id = name_to_id(username)
        rows = ["userID", "status"]
        values = ["{}".format(str(my_id)), 
                  "{}".format(status)]
        conn.insert("Status", rows, values)
        print("Done: update_status")
    except Exception as e:
        print(e)
        print("Fail: update_status")

def fetch_my_status(username):
    """
    fetch_my_status("'David'")
    """
    try:
        my_id = name_to_id(username)
        status = conn.query('Status', ["status", "ts"], conditions=['''userID=''' + str(my_id)], 
                                    order=["{}".format('ts'), "DESC"])[0]
        print(status)
                                
    except Exception as e:
        print(e)
        print("Fail: fetch_my_status")

def fetch_my_location(username):
    """
    fetch_my_location("'David'")
    """
    try:
        my_id = name_to_id(username)
        location = conn.query('Location', ["location", "ts"], conditions=['''userID=''' + str(my_id)], 
                                    order=["{}".format('ts'), "DESC"])[0]
        print(location)
                                
    except Exception as e:
        print(e)
        print("Fail: fetch_my_status")

def generate_code(username):
    try: 
        my_id = name_to_id(username)
        conn.delete('AddCode', ['''userID={}'''.format(my_id)])
        my_code = repr(coder.getCode(username))
        rows = ["userID", "code"]
        values = ["{}".format(username), "{}".format(my_code)]
        conn.insert("AddCode", rows, values)
    except Exception as e:
        print(e)
        print("Fail: generate_code")

def add_friend(username, mycode):
    my_id = name_to_id(username)
    friend_id = conn.query('AddCode', ["userID"], 
              conditions=['''code={}'''.format(mycode)])
    print(my_id, friend_id)
    
    rows = ["userID", "friendID"]
    values = ["{}".format(my_id), "{}".format(friend_id)]
    conn.insert("Friends", rows, values)

    rows = ["userID", "friendID"]
    values = ["{}".format(friend_id), "{}".format(my_id)]
    conn.insert("Friends", rows, values)

    conn.delete("AddCode", ['''userID={}'''.format(friend_id)])

    print(conn.query("Friends", "*"))
    print(conn.query("AddCode", "*"))

def auto_deletion():
    # (ID, datetime.datetime.obj, detail)
    conn.delete("Location", ['''ts < (NOW() - INTERVAL 10 MINUTE)'''])
    conn.delete("AddCode", ['''ts < (NOW() - INTERVAL 10 MINUTE)'''])
    conn.delete("Status", ['''ts < (NOW() - INTERVAL 10 MINUTE)'''])



conn.debugging()
generate_code()