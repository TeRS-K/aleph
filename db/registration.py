from Connector import Connection

conn = Connection("18.216.32.253", "root", "password", "test")

def create_new(username, password):
    rows = ["username", "hashedpw"]
    values = ['"' + username + '"', '"' + password + '"']
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

rows = ["username", "hashedpw"]
values = ["'David'", "'Duan'"]

conn.insert("Login", rows, values)

rows = ["username", "hashedpw"]
values = ["'Ban'", "'Duan'"]

conn.insert("Login", rows, values)
"""
print(conn.query('Login', '*'))
rows = ["username", "hashedpw"]
values = ["'David'", "'Duan'"]
conn.insert("Login", rows, values)
print(conn.query('Login', '*'))

rows = ["username", "hashedpw"]
values = ["'David'", "'Duan'"]
conn.insert("Login", rows, values)
print(conn.query('Login', '*'))

rows = ["username", "hashedpw"]
values = ["'Duan'", "'Duan'"]
conn.insert("Login", rows, values)
print(conn.query('Login', '*'))
