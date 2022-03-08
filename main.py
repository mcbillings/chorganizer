from heapq import *
from chores import *
import csv
import random

chores = []
people = ['Mikayla', 'Spencer', 'Owen']

with open('chores.csv', newline='') as choreFile:
    choreReader = csv.reader(choreFile)
    for row in choreReader:
        thisChore = Chore(row[0], row[1], row[2])
        chores.append((thisChore.priority, id(thisChore), thisChore))

heapify(chores)

random.shuffle(people)

for person in people:
    print(person + ": " + chores.pop()[2].name)


        
         



