def strcounter(s):
    for sym in set(s):
        counter = 0
        for syb in s:
            if sym == syb:
                counter += 1
        print(sym, counter)
strcounter('bacc')

def strcounter_new(s):
    sums = {}
    for sym in s:
        sums[sym] = sums.get(sym, 0) + 1
    for sym, count in sums.items():
        print(sym, count)
strcounter_new('bacc')
