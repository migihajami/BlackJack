

class TestClass:
    staticvar = ["test"]


ttt = TestClass()
yyy = TestClass()
print(f"ttt - {ttt.staticvar}")
print(f"yyy - {yyy.staticvar}")

ttt.staticvar.append("test1")

print(f"ttt - {ttt.staticvar}")
print(f"yyy - {yyy.staticvar}")
