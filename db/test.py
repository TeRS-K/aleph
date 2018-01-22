from db.Connector import Connection

conn = Connection("18.216.32.253", "root", "password", "test")


values = ["'Felix'", "'V1'", "'Dead'"]

conn.insert("people", values)



conn.delete("people", ['''name="Emily"'''])


print(conn.query("people", "*"))
