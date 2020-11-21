a = "Hi"
b = "there"

c = "{} {{}} {}!".format(a,b)

print(c)

15 > 0 is True #False
# same as 0 < 15 and 0 == True. 0<15 - true. 0==True - false. True and False - false.

def tricky_func(a=[]):
        a.append(1)
        print(a)

tricky_func()
tricky_func()