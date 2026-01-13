score = [
[15,12,20],
[20,17,18],
[20,16,19]
]

print("My total scores for each subject:")
for row in score:
    print(sum(row))
print('\n')
print("My average for each subject:")
for row in score:
    average = sum(row)/len(row)
    print(average)
print('\n')
print("My lowest score:")
lowest = []
for row in score:
    lowest.append(min(row))
print(min(lowest))
