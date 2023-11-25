import pandas as pd

# read the tents-preference list csv
tentPrefsDf = pd.read_csv("tents-prefs.csv", header=None)
tentSizeDf = pd.read_csv("tents-sizes.csv", header=None)

# convert to a new datastructure with just names
names = []
for _ in tentPrefsDf[0]:
    if _ not in names:
        names.append(_)

tents = {}
tentKey = []
tentSize = []

for i in tentSizeDf[0]:
    tentKey.append(i)

for j in tentSizeDf[1]:
    tentSize.append(j)

tentIndex = 0
for k in tentKey:
    tents[k] = tentSize[tentIndex]
    tentIndex += 1


# highAffinityPersons = tentPrefsDf[tentPrefsDf[2] >= 5]

# for name in names:
#     print(tentPrefsDf.loc[tentPrefsDf[1] == name])

# combinations of people that should be avoided...
lowAffinityPersons = tentPrefsDf[tentPrefsDf[2] == 0]
troubleMakers = {}
haters = []
dislikes = []
for hater in lowAffinityPersons[0]:
    haters.append(hater)

for disliked in lowAffinityPersons[1]:
    dislikes.append(disliked)


dislikedIndex = 0
for hater in haters:
    troubleMakers[hater] = dislikes[dislikedIndex]
    dislikedIndex += 1


print(troubleMakers)

## learn to

def assignTents():
    

def calculateHappiness():


# def main():
    
    


# main()