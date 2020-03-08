import hashlib

# m = hashlib.md5("hello alex".encode("utf-8"))
#
# print(m.hexdigest())
m = hashlib.md5()
m.update(b"hello alex")
print(m.hexdigest())
m.update("欢迎来到小猿圈".encode("utf-8"))
print(m.hexdigest())

m2 = hashlib.md5()
m2.update("hello alex欢迎来到小猿圈".encode("utf-8"))
print(m2.hexdigest())