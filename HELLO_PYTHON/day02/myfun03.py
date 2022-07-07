import random


def getHollJJak() :
    ret = ""
    rnd = random.random()
    if rnd > 0.5 :
        ret = "홀"
    else :
        ret = "짝"
    return ret
com = getHollJJak()
print("com",com)