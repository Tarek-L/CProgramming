from timeit import timeit

nums = list(range(10000))

print(timeit(
    "d={}; [d.__setitem__(x,d.get(x,0)+1) for x in nums]",
    globals=globals(),
    number=100
))

print(timeit(
    "d={}; [d.__setitem__(str(x),d.get(str(x),0)+1) for x in nums]",
    globals=globals(),
    number=100
))
