#n = months (mating cycles) k = pairs per cycle, start with one pair, reproductive after 1 month
n = input("How many mating cycles?")
k = input("How many offspring per cycle?")
p = 1
rabbits = [1,1]
for num in range(2,n):
    a = rabbits[num - 1] + k * rabbits[num - 2]
    rabbits.append(a)

print rabbits[n-1]


