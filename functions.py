# this is the list of all the functions needed for the program
import re

syllable_regex = re.compile("[^aeiouy]*[aeiouy]+(?:[^aeiouy]*$|[^aeiouy](?=[^aeiouy]))?", re.IGNORECASE)

# compare syllables without order - weight less
def fuzzy_syllable_list(name, newName):
    name = name.lower()
    newName = newName.lower()
    score = 0 
    nameSList = syllable_regex.findall(name)
    newNameSList = syllable_regex.findall(newName)
    for syllable in nameSList: 
        if syllable in newNameSList:
            score += 1
    return score

# compare syllables with order - weight more
def syllable_list(name, newName):
    name = name.lower()
    newName = newName.lower()
    score = 0
    nameSList = syllable_regex.findall(name)
    newNameSList = syllable_regex.findall(newName)

    try:
        for i in range(len(nameSList)):
            if nameSList[i] == newNameSList[i]:
                score += 1
    except:
        pass

    return score

def similarity(name, newName):
    name = name.lower()
    newName = newName.lower()
    score = 0
    for i in range(5):
        if name[:i] in newName[:i]:
            score += 1
        if name[-i:] in newName[-i:]:
            score += 1
    return score

def middleSimilarity(name, newName):
    name = name.lower()
    newName = newName.lower()
    score = 0
    nameSet = set(name[1:-1])
    #print(nameSet)
    for middle in newName[1:-2]:
        if middle in nameSet:
            score += 1
    return score
