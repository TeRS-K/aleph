"""
friend name listed

fetch friend.status
fetch friend.location
update self.status
update self.location

add friend
wait for Felix's wrapper for code

delete friend

delete account 

send location using google map api
text api send message 

count function as reinforcement learning

"""
from Connector import Connection

conn = Connection("18.216.32.253", "root", "password", "test")

def fetch_friend_status(username, friend) :
    """
    username: your name
    friend: your friend's name
    """
    try:
        # SELECT <userID> FROM Login WHERE username = <friend_id>
        # This step checks if your friend exists.
        friend_id = conn.query('Login', ["userID"], ['''username=''' + friend])
    
        try:
            # SELECT <userID> FROM Friends WHERE friendID = <friend_id>
            # This step checks if you are friends with your friend.
            is_friend = conn.query('Friends', ["userID"], ['''friendID=''' + friend_id])
       
            try:
                # order by
                status = conn.query('Status', ["userID"], order=["{}".format(friend_id), "ASC"] )
                print("Get friend's status successfully.")
                return status   
            except:
                pass

        except Exception as e:
            print("Fail: fetch_friend_status - You two are not friends.")
    
    except:
        print("Friend does not exist.")
    


def fetch_friend_location(username, friend) :

    try:
        friend_id = conn.query('Login', ["userID"], ['''username=''' + friend])
    
        try:
            is_friend = conn.query('Friends', ["userID"], ['''friendID=''' + friend_id])
       
            try:
                # order by
                status = conn.query('Location', ["userID"], order=["{}".format(friend_id), "ASC"])
                print("Get friend's location successfully.")
                return status 
            except:
                pass
        except:
            print("You two are not friends.")
    
    except:
        print("Friend does not exist.")
    

def delete_account(username) :
    # pop_up:
    # this process is invertible; type the following statement to proceed
    # 
    confirmation = input()
    if (confirmation == "Y"):
        conn.delete("Login", ['''username={}'''.format(username)])
    
    # check if other table has updated as well.


def delete_friend(username, friend) :
    try:
        my_id = conn.query('Login', ["userID"], ['''username=''' + username])[0][0]
        # print(my_id)
        friend_id = conn.query('Login', ["userID"], ['''username=''' + friend])[0][0]
        # print(friend_id)
        # print('''username:''' + str(my_id))
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

'''
rows = ["username", "hashedpw"]
values = ["'David'", "'Duan'"]
conn.insert("Login", rows, values)

rows = ["username", "hashedpw"]
values = ["'Felix'", "'Zhou'"]
conn.insert("Login", rows, values)

rows = ["userID", "friendID"]
values = ["100038", "100039"]
conn.insert("Friends", rows, values)
debugging()
delete_friend("'David'", "'Felix'")
debugging()

delete_account("'David'")
debugging()

rows = ["username", "hashedpw"]
values = ["'David'", "'Duan'"]
conn.insert("Login", rows, values)

rows = ["username", "hashedpw"]
values = ["'Felix'", "'Zhou'"]
conn.insert("Login", rows, values)

rows = ["username", "hashedpw"]
values = ["'A'", "'B'"]
conn.insert("Login", rows, values)

rows = ["username", "hashedpw"]
values = ["'C'", "'D'"]
conn.insert("Login", rows, values)

'''

def debugging():
    print(conn.query('Login', '*'))
    print(conn.query('Friends', '*'))
    print(conn.query('Location', '*'))
    print(conn.query('Status', '*'))


"""
rows = ["userID", "friendID"]
values = ["100040", "100042"]
conn.insert("Friends", rows, values)
rows = ["userID", "friendID"]
values = ["100040", "100044"]
conn.insert("Friends", rows, values)
rows = ["userID", "friendID"]
values = ["100040", "100045"]
conn.insert("Friends", rows, values)
rows = ["userID", "friendID"]
values = ["100040", "100046"]
conn.insert("Friends", rows, values)
"""

rows = ["userID", "location"]
values = ["100044", "'DC'"]
conn.insert("Location", rows, values)

debugging()
fetch_friend_status