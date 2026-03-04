score = [
[15,12,20],
[20,17,18],
[20,16,19]
]

Math = score[0]
Science = score[1]
Music = score[2]

print(f'Math = {Math}\nScience = {Science}\nMusic = {Music}')
print("\n")

Day1 = [row[0] for row in score]
Day2 = [row[1] for row in score]
Day3 = [row[2] for row in score]

print(f'Day 1 scores = {Day1}, \nDay 2 scores = {Day2}, \nDay 3 scores = {Day3}, ')
print('\n')

Daytot1 = sum([row[0] for row in score])
Daytot2 = sum([row[1] for row in score])
Daytot3 = sum([row[2] for row in score])

Mathtot = sum(score[0])
Scitot = sum(score[1])
Musictot = sum(score[2])

Mathav = sum(score[0])/len(score[0])
Sciav = sum(score[1])/len(score[1])
Musicav = sum(score[2])/len(score[2])

print(f'Total scores for each subject and day:\n')
print(f'Math = {Mathtot}\nScience = {Scitot}\nMusic = {Musictot}')
print(f'\nDay 1 = {Daytot1}\nDay 2 = {Daytot2}\nDay 3 = {Daytot3}')

print(f'\nAverage scores in each subject:\n')
print(f'Math = {Mathav}\nScience = {Sciav}\nMusic = {Musicav}')
