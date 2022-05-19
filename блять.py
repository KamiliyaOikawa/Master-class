data = ("O!", "Megacom", "0705", "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543")
designations = []
codes = []
for i in data:
    if i[0] == '0':
        codes.append(i)
    else:
        designations.append(i)
operators = {}
c = 0
while c != len(codes):
    operators[designations[c]] = codes[c]
    c += 1
del operators['Katel'], operators['Fonex']
operators['O!'] = {'0700', '0705', '0500'}
operators['Megacom'] = {'0550', '0999', '0555'}
operators['Beeline'] = {'0770', '0222', '0777'}
for k, v in operators.items():
    print(f'{k} - {v}')