from Generator import Hasher, Coder

hasher = Hasher()

print(hasher.hash("David", "Password"))
print(hasher.hash("TIU", "Password"))
print(hasher.hash("FOO", "Password"))
print(hasher.hash("SIU", "Password"))
print(hasher.hash("David", "Password"))


coder = Coder()

print(coder.getCode("David"))
print(coder.getCode("David"))
print(coder.getCode("Teresa"))
print(coder.getCode("Teresa"))