names = ["Me", "Lia", "Jake"]

steps = [

  [4500, 5200, 4800, 5000, 5300],

  [4000, 4100, 3900, 4200, 4600],

  [6000, 5800, 5900, 6100, 6200]

]

#Rows are the steps for the respective person, and Columns are the days.

me = steps[0]
lia = steps[1]
jake = steps[2]

print(f'Me = {me}\nLia = {lia}\nJake = {jake}')
print("\n\n")

for stepcount,runner in zip(steps,names):
    total = sum(stepcount)
    print(f'{runner} = {total} steps!')

calcs = [sum(people) for people in steps]
winval = max(calcs)
loseval = min(calcs)
winperson = calcs.index(winval)
loseperson = calcs.index(loseval)
print("\nMost steps:",names[winperson])
print("Least steps:",names[loseperson])

diff = winval - loseval
print(f'\nDifference between highest step count and lowest step count: {diff}')
