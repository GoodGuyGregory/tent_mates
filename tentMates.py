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


def getDislikedCampers(campers, camper):
    for camper in campers:
        print(tentPrefsDf.loc[tentPrefsDf[1] == camper])

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

    return haters


def getLovedCampers(campers, camper):
    for camper in campers:
        print(tentPrefsDf.loc[tentPrefsDf[1] == camper])

    # combinations of people that shouldn't be avoided...
    highAffinityPersons = tentPrefsDf[tentPrefsDf[2] >= 5]
    troubleMakers = {}
    lovers = []
    dislikes = []
    for lover in highAffinityPersons[0]:
        lovers.append(hater)

    for disliked in lowAffinityPersons[1]:
        dislikes.append(disliked)

    dislikedIndex = 0
    for hater in haters:
        troubleMakers[hater] = dislikes[dislikedIndex]
        dislikedIndex += 1

    return haters


# assigns tents to each camper with a mild heuristic for affinity
def assignTents(tentsAvailable, campers):
    tentsWithCampers = {}

    for tent in tentsAvailable:
        campersPerTent = []
        while tentsAvailable[tent] > 0:
            camper = random.choice(campers)
            if len(campersPerTent) > 0:
                # calculate the lovers and fighters within the tent
                # fighters:
                # people to not put in the same tent:
                fighters = getDislikedCampers()

                lovers = getLovedCampers(camp)
            else:
                # just assign as no-one is in the tent
                campersPerTent.append(camper)

            campers.remove(camper)
            tentsAvailable[tent] -= 1

        tentsWithCampers[tent] = campersPerTent

    return tentsWithCampers


# returns the calculated sum of the affinity for each name
def calculateHappiness(campersInTents, tents):
    # check each camper's happiness based on tents occupants
    happiness = 0

    # per tent check the happiness of the occupants. add to happiness
    for occupants in campersInTents.values():
        ## check the other occupants preference
        for camper in occupants:
            print(getCamperAttitude(camper, occupants))
            happiness += getCamperAttitude(camper, occupants)

    return happiness


# check each other camper's preference fpr each camper in the tent
def getCamperAttitude(camper, occupants):
    camperHappiness = 0
    camperPreferences = tentPrefsDf[tentPrefsDf[0] == camper]

    for i in range(len(occupants)):
        if occupants[i] != camper:
            score = camperPreferences[camperPreferences[1] == occupants[i]][2].tolist()
            if len(score) > 0:
                camperHappiness += score[0]

    return camperHappiness


def main():
    campers = getCamperNames()
    tents = getTentConfigurations()
    score = 0

    while score < 175:
        tentsWithCampers = assignTents(tents, campers)
        score = calculateHappiness(tentsWithCampers, tents.keys())
        print(score)


main()
