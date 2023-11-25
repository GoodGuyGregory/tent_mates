import pandas as pd
import random


# read the tents-preference list csv
tentPrefsDf = pd.read_csv("tents-prefs.csv", header=None)

tentSizeDf = pd.read_csv("tents-sizes.csv", header=None)


def getCamperNames():
    # convert to a new datastructure with just names
    names = []
    for _ in tentPrefsDf[0]:
        if _ not in names:
            names.append(_)

    return names


def getTentConfigurations():
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

    return tents


# highAffinityPersons = tentPrefsDf[tentPrefsDf[2] >= 5]

# for name in names:
#     print(tentPrefsDf.loc[tentPrefsDf[1] == name])

# combinations of people that should be avoided...
# lowAffinityPersons = tentPrefsDf[tentPrefsDf[2] == 0]
# troubleMakers = {}
# haters = []
# dislikes = []
# for hater in lowAffinityPersons[0]:
#     haters.append(hater)

# for disliked in lowAffinityPersons[1]:
#     dislikes.append(disliked)


# dislikedIndex = 0
# for hater in haters:
#     troubleMakers[hater] = dislikes[dislikedIndex]
#     dislikedIndex += 1


# print(troubleMakers)


# assigns tents to each camper with a mild heuristic for affinity
def assignTents(tentsAvailable, campers):
    tentsWithCampers = {}

    for tent in tentsAvailable:
        while tentsAvailable[tent] > 0:
            camper = random.choice(campers)
            tentsAvailable[tent] -= 1
            campers.remove(camper)
            tentsWithCampers[camper] = tent

    print(tentsWithCampers)
    return tentsWithCampers


# returns the calculated sum of the affinity for each name
def calculateHappiness(campersInTents, tents):
    # check each camper's happiness based on tents occupants
    happiness = 0

    print(tents)

    return 0


def main():
    campers = getCamperNames()
    tents = getTentConfigurations()
    score = 0

    tentsWithCampers = assignTents(tents, campers)

    score = calculateHappiness(tentsWithCampers, tents.keys())


main()
