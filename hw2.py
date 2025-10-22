from logging import setLoggerClass


def union(set1, set2):
    ret = []
    for num in set1:
        ret.append(num)
    for num in set2:
        if num not in ret:
            ret.append(num)
    return ret

def intersection(set1, set2):
    ret = []
    for num in set1:
        if num in set2:
            ret.append(num)

    return ret

def complement(set, universal):
    ret = []
    for num in universal:
        if num not in set:
            ret.append(num)
    return ret

def difference(minuend, subtrahend):
    return complement(subtrahend, minuend)


def problem_14():
    s = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    a = {0, 2, 4, 6, 8}
    b = {1, 3, 5, 7, 9}
    c = {2, 3, 4, 5}
    d = {1, 6, 7}


    print(sorted(union(a, c)))
    print(sorted(intersection(a, b)))

    print(complement(c, s))

    print( sorted(union( intersection(complement(c, s), d ), b )))

    print(complement(intersection(s,c), s))

    print(intersection(intersection(a, c),complement(d,s)))


def problem_15():
    s = {"copper", "sodium", "nitrogen", "potassium",
         "uranium", "oxygen", "zinc"}
    a = {"copper", "sodium", "zinc"}
    b = {"sodium", "nitrogen", "potassium"}
    c = {"oxygen"}

    print(complement(a,s))

    print(union(a,c))

    print(union(intersection(a,complement(b, s)),complement(c,s)))

problem_15()