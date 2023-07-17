from greenlet import greenlet


def func1():
    print("1. 1")
    gr2.switch()
    print("1. 2")
    gr2.switch()


def func2():
    print("2. 1")
    gr1.switch()
    print("2. 2")
    gr1.switch()


gr1 = greenlet(func1)
gr2 = greenlet(func2)

gr1.switch()
