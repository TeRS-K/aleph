from Connector import Connection

conn = Connection("18.216.32.253", "root", "password", "test")

rows = ["username", "hashedpw"]
values = ["'David'", "'Duan'"]

conn.insert("Login", rows, values)



# conn.delete("people", ['''name="Emily"'''])


print(conn.query("Login", "*"))
