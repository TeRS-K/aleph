from Generator import Hasher

hasher = Hasher()

print(hasher.hash("David", "Password"))
print(hasher.hash("TIU", "Password"))
print(hasher.hash("FOO", "Password"))
print(hasher.hash("SIU", "Password"))
print(hasher.hash("David", "Password"))