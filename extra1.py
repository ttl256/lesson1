def f(lst):
    while True:
        for i in lst:
            # Generator keeps state. for is defined for a gen.
            yield i

a=[1,2,3]
gen = f(a)

# print(gen[1])
# You can't access a specific element in a gen.

for i in gen:
    print(i)