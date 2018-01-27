from Connector import Connection

conn = Connection("18.216.32.253", "root", "password", "test")

rows = ["username", "hashedpw"]
values = ["'David'", "'Duan'"]

conn.insert("Login", rows, values)


print(conn.query("Login", "*", conditions=["username <> 'SIU'"] ,order=["username", "ASC"]))


conn.delete("Login", ['''username="David"'''])


print(conn.query("Login", "*"))
