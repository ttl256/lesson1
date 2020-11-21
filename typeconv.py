print(float("1")) # str->float works fine
print(int(float("2.5"))) #int("2.5") str->int doesn't work, because we need to convert like this str->float->int
print(bool(1))
print(bool(''))
print(bool(0))