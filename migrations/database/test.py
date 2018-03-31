from Connector import Connection
from database import *

conn = Connection("18.216.32.253", "root", "password", "test")

"""
rows = ["username", "hashedpw"]
values = ["'David'", "'Duan'"]

conn.insert("Login", rows, values)

print(conn.query("Login", "*", conditions=["username <> 'SIU'"] ,order=["username", "ASC"]))

conn.update("Login", ["username='Poo'", "hashedpw='PLOP'"], ["username='David'"])

print(conn.query("Login", "*"))

print(conn.query("Login", "*"))

print(guessLocation(100113))

print(conn.query("Frequency", ["frequency"], ["userID=100113", "location='MC'"]))
"""

# conn.delete("Login", ['''username="Poo"'''])

# conn.deleteall()

conn.deleteall()
new_user("'Lila'", "'pwlila'")
new_user("'David'", "'pwdavid'")
log_in("'David'", "'pwdavid'")
code = generate_code("'Lila'")
add_friend("'David'", code)
update_location("'David'", "'Princeton'")
update_status("'David'", "3")
print(fetch_location("'David'"))
print(fetch_status("'David'"))
print(fetch_friend_location("'Lila'", "'David'"))
print(fetch_friend_status("'Lila'", "'David'"))
update_location("'David'", "'Waterloo'")
update_status("'David'", "4")
print(fetch_location("'David'"))
print(fetch_status("'David'"))
print(fetch_friend_location("'Lila'", "'David'"))
print(fetch_friend_status("'Lila'", "'David'"))
delete_friend("'David'", "'Lila'")
conn.debugging()
conn.deleteall()
