import collections

hand = input().split()
firstC = []
i = 0
#print(len(hand))
for i in range(len(hand)):
    temp = list(hand[i])
    firstC.append(temp[0])

#print(hand)
#print(firstC)
counter = collections.Counter(firstC)
bla = counter.most_common(1)
#print(counter)
#print(str(bla))
mCommon = list(str(bla))
print(mCommon[7])
#print(mCommon)