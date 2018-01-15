from db.Connection import Connection

conn = Connection("18.216.32.253", "root", "password", "test")

'''
values = ["Jane", "Aaron's", "Completely Enamoured"]

conn.insert("people", values)
'''

print(conn.query("people", "*", ["status='Depressed'"])[0][:])
