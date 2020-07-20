idOfStudents = input().split(" ")
subjectScores = input().split(" ")
idOfStudents = (map(int, idOfStudents))
subjectScores = (map(int, subjectScores))
iterable = zip(idOfStudents, subjectScores)
inputFormat = []
for i in iterable:
  inputFormat.append(list(i))
print(inputFormat)
inputFormat = sorted(inputFormat)
inputFormat = inputFormat[::-1]
print(inputFormat)
dictionary = {}                                  #A empty dictinary is set to get the output as {id : [scores]}
for item in range(len(inputFormat)):
    print(inputFormat[item])
    iterationPossible = inputFormat[item]
    keys, values = iterationPossible[0], iterationPossible[1]
    print(keys, values)
    if keys in dictionary:
        dictionary[keys].append(values)
    else:
        dictionary[keys] = [values]
        print(dictionary)                    #Getting Dictionary 0utput of format{id:[list of scores in descending order]}
print(dictionary)
getElements = dictionary.values()
count = 0
elementsWeGet = []
scoredSum = []
sum = 1
for i in getElements:
    elementsWeGet.append(i)
print(elementsWeGet)
for c in elementsWeGet:
    print(c)
    counter = 0
    for getCounter in range(0, 5):                           # range is 0,5 to get all the 5 subject scores
        counter = counter+c[getCounter]
    sum = counter/5
    scoredSum.append(sum)
print(scoredSum)                                             # gives us the scored sum the average of top 5 marks
IdList = dictionary.keys()
IdList = list(IdList)
print(IdList)
ZipItr = zip(IdList, scoredSum)                              # zipped id and average of top 5 together
finalList = list(ZipItr)
print(finalList)                                             #Final Answer in A list


# SOLUTION 2 BUT IT Has one bug we are able to have only maximum of d*n characters like id of 1 would have 5 scores then id of 2 would also have 5 scores unlike the problem 
# id should be same and repeating value should be also same


# d = abs(int(input("Enter Num of Subjects")))
# completeListsAccordingToInput = []

# if d >= 5:
#   n = int(input("Enter the Number of Students"))
#   for i in range(0, n):
#     for b in range(0, d):
#       idStudents = int(input("ID"))
#       scoresStudents = float(input("Score"))
#       createdList = [idStudents, scoresStudents]
#       completeListsAccordingToInput.append(createdList)
#   totalCombinations = d*n
#   completeListsAccordingToInput = sorted(completeListsAccordingToInput)
#   completeListsAccordingToInput = completeListsAccordingToInput[::-1]
#   print(completeListsAccordingToInput)
# # Until This Stage Everything is Input 

#   dictionary = {}                                  #A empty dictinary is set to get the output as {id : [top 5 scores only]}
#   for item in completeListsAccordingToInput:
#     print(item)
#     keys, values = item[0], item[1]
#     print(keys, values)
#     if keys in dictionary:
#       dictionary[keys].append(values)
#     else:
#       dictionary[keys] = [values]
#   print(dictionary)                                #GEtting Dictionary 0utput
#   getElements = dictionary.values()
#   count = 0
#   elementsWeGet = []
#   scoredSum = []
#   sum = 1
#   for i in getElements:
#     elementsWeGet.append(i)
#   print(elementsWeGet)
#   for c in elementsWeGet:
#     print(c)
#     counter = 0
#     for getCounter in range(0, 5):
#       counter = counter+c[getCounter]
#     sum = counter/5
#     scoredSum.append(sum)
#   print(scoredSum)
#   IdList = dictionary.keys()
#   IdList = list(IdList)
#   print(IdList)
#   ZipItr = zip(IdList, scoredSum)
#   finalList = list(ZipItr)
#   print(finalList)
# else:
#   print("A minimum of 5 subjects are required")

