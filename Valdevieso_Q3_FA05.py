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

print(f'Me = {me}\nLia = {lia}\nJake = {jake}\n')

print("\n")


for daycount in range(len(steps[0])):
    total = 0
    for person in range(len(steps)):
        total += steps[person][daycount]
    print("Day", daycount+1, "total steps:", total)
print("\n")

best_day = 0
best_total = 0

for col in range(len(steps[0])):
    total = 0
    for row in range(len(steps)):
        total += steps[row][col]
    
    if total > best_total:
        best_total = total
        best_day = col

print("Best day:","Day",best_day+1)
