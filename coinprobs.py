

import collections

def problems():
    denoms = [1, 5, 10, 25, 50]
    for q01 in range(100):
        for q05 in range(20):
            for q10 in range(10):
                for q25 in range(4):
                    for q50 in range(2):
                        combo = [q01, q05, q10, q25, q50]
                        total = sum([count*den for count, den in zip(combo, denoms)])
                        if 0 < total < 100:
                            yield (sum(combo), total)

counts = collections.Counter(problems())

for count in range(100):
    print(''.join([str(counts.get((count, value), ' ')) for value in range(100)]))
#for blah in sorted(counts.items(), key=lambda x: -x[1]):
#    print(blah)
#    break

#print(counts.get((5, 12), None))

#for xx in problems():
#    print(xx)


