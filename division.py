from __future__ import division


def make_division_by(n):
    def division(x):
        return x/n
    return(division)

division_by_3 = make_division_by(3)
print(division_by_3(18))

