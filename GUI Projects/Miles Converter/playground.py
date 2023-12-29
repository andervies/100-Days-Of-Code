


def add(*args):
    summary = 0
    for n in args:
        summary += n
    print(summary)


print(add(2, 3, 4, 6, 6))