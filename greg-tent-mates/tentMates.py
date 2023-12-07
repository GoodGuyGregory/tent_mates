import pandas as pd
import random
import copy
import pprint

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
    # print(tentPrefsDf.loc[tentPrefsDf[1] == camper])

    # combinations of people that should be avoided...
    lowAffinityPersons = tentPrefsDf[(tentPrefsDf[2] <= 3) & (tentPrefsDf[1] == camper)]
    # print(lowAffinityPersons)
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
    # combinations of people that shouldn't be avoided...
    highAffinityPersons = tentPrefsDf[
        (tentPrefsDf[2] >= 8) & (tentPrefsDf[1] == camper)
    ]
    closeFriends = {}
    lovers = []
    likes = []
    for lover in highAffinityPersons[0]:
        lovers.append(lover)

    for liked in highAffinityPersons[1]:
        likes.append(liked)

    likedIndex = 0
    for lover in lovers:
        closeFriends[lover] = likes[likedIndex]
        likedIndex += 1

    return lovers


# assigns tents to each camper with a mild heuristic for affinity
def assignTents(tentsAvailable, campers):
    campersWithTents = {}

    referenceList = copy.deepcopy(campers)

    for tent in tentsAvailable:
        campersPerTent = []
        while tentsAvailable[tent] > 0:
            camper = random.choice(campers)
            if len(campersPerTent) > 0:
                # calculate the lovers and fighters within the tent
                # fighters:
                # people to not put in the same tent:
                fighters = getDislikedCampers(referenceList, camper)

                if any(x in fighters for x in campersPerTent):
                    lessAgressiveCampers = [i for i in campers if i not in fighters]
                    choosenCamper = random.choice(lessAgressiveCampers)
                    campersWithTents[camper] = tent
                    campersPerTent.append(choosenCamper)
                    campers.remove(choosenCamper)
                else:
                    campersWithTents[camper] = tent
                    campersPerTent.append(camper)
                    campers.remove(camper)
            else:
                # just assign as no-one is in the tent
                campersWithTents[camper] = tent
                campersPerTent.append(camper)
                campers.remove(camper)

            tentsAvailable[tent] -= 1

    return campersWithTents


def swapForHappierCampers(campersWithTents, campers):
    for camper in campersWithTents:
        campersTent = campersWithTents[camper]
        # check each occupant and look for their favorite person.. 8 <= value
        lovedCampers = getLovedCampers(campers, camper)
        # if any(likedCamper in lovedCampers for likedCamper in tentsWithCampers[likedCamper]):

        for k, v in campersWithTents.items():
            if k in lovedCampers:
                if v not in campersTent:
                    oldTent = campersWithTents[k]
                    campersWithTents[k] = campersTent
                    # find all people with the campers tent.
                    otherCampersSameTent = otherCampersInTent = [
                        p
                        for p, t in campersWithTents.items()
                        if (t == campersTent) and (p != camper)
                    ]
                    if len(otherCampersSameTent) > 1:
                        campersToSwap = [
                            person
                            for person in otherCampersSameTent
                            if person not in lovedCampers
                        ]
                        if len(campersToSwap) > 0:
                            camperToSwap = random.choice(campersToSwap)
                            campersWithTents[camperToSwap] = oldTent
                        else:
                            continue
                    else:
                        campersWithTents[otherCampersSameTent[0]] = oldTent

    return campersWithTents


# returns the calculated sum of the affinity for each name
def calculateHappiness(tentsWithCampers, tents):
    # check each camper's happiness based on tents occupants
    happiness = 0

    # per tent check the happiness of the occupants. add to happiness
    for camper in tentsWithCampers.keys():
        ## check the other occupants preference
        campersTent = tentsWithCampers[camper]
        otherCampersInTent = [
            k for k, v in tentsWithCampers.items() if v == campersTent
        ]
        for camper in otherCampersInTent:
            happiness += getCamperAttitude(camper, otherCampersInTent)

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

    campersWithTents = assignTents(tents, campers)
    score = calculateHappiness(campersWithTents, tents.keys())

    while score < 175:
        swapForHappierCampers(campersWithTents, campers)
        score = calculateHappiness(campersWithTents, tents.keys())

    print(score)
    pprint.pprint(campersWithTents)


main()
