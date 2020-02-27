data = [['a','b','c'],
        ['a','b']
        ]


lenSize = len(data[0])
comparingState = True

for d in data:
    if lenSize != len(d):
        comparingState = False
    else:
        pass
print(comparingState)
