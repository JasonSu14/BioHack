import re
import functions
import database

newName = input("Enter a new drug name: ")
Dictionary = {}

for existingNames in database.databaseA:
    score = 0
    score += functions.similarity(existingNames, newName)
    score += functions.middleSimilarity(existingNames, newName)
    score += functions.syllable_list(existingNames, newName)
    score += functions.fuzzy_syllable_list(existingNames, newName)
    Dictionary[existingNames] = score # builds dict with score and name of drug

Dictionary = sorted(Dictionary.items(), key=lambda x: x[1], reverse=True)
top = dict(Dictionary[:5]) # takes off the top 5 or whatever
print(top)

if set(newName) in ['y', 'h', 'k', 'j', 'w']:
    print("The following letters do not translate well to other langauges: y, h, k, j, w. Consider alternatives if possible.")

if newName[-1] in ['l', 'z', 'b', 's', 't', 'i']:
    print("The final letter in the new name is often confused with numbers when written close to a dosage. Consider alternatives if possible. Letters: l, z, b, s, t, i.")

selfscore = 0
selfscore += functions.similarity(newName, newName)
selfscore += functions.middleSimilarity(newName, newName)
selfscore += functions.syllable_list(newName, newName)
selfscore += functions.fuzzy_syllable_list(newName, newName)

print("The top similarity is " + f"{(Dictionary[0][1]/selfscore *100):.2f}" + r"% similar.")
