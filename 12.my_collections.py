from collections import Counter, defaultdict

data = ['a','b','a','c']
counter = Counter(data)
print(counter)

dd = defaultdict(int)
dd['missing'] += 1
print(dd['missing'])