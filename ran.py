import random as r

light = False

y=0
while not light:
    random_set = []
    x=0
    while x < 3:
        random_set.append(r.randint(1,100))
        x+=1
    
    if random_set == [1,2,3]:
        for number in random_set:
            light = True
            with open('record.txt', 'a') as f:
                print(f'{y + 1}', file=f)
    y+=1

