def foo (a):
    res = [i for i in range(a) if i % 2]
    return res

k = len(foo(7))

print(foo(7))
print(k)
