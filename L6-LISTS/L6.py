dowolna = 1
dow = 0
strt = 'słowo'
lists = [9854, 'fod', 75, 'fud', 65, dowolna]
print(lists)
print(lists[1])
lists[4] = lists[0]
print(lists)
print(strt[1], [6, 5])
print(lists * 2)

while dow < len(lists):
    print(lists[dow])
    dow += 1

lists.append([991, 'io9'])
print(lists[6][0])
print(lists[6][1])

lists.insert(6,strt)
ugaboga = lists.index(75)
print(ugaboga)

