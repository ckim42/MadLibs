def getNounInput():
    return input("Enter a noun ")

def getVerbInput():
    return input("Enter a verb in the past tense ")

def getAdjInput():
    return input("Enter an adjective ")

def getWordInput(type):
    if (type == "noun"):
        return getNounInput()
    if (type == "verb"):
        return getVerbInput()
    if (type == "adj"):
        return getAdjInput()

lib = '''The %s singer walked to the coffeeshop
 and bought a pricey %s. The paparazzi %s joyfully.
 They photographed him mid-bite. It made headlines
 the next
 day''' #.format(getAdjInput(),getNounInput(),getVerbInput())
words = []
wordsNeeded = ["adj", "noun", "verb"]
for x in wordsNeeded:
    words.append(getWordInput(x))

lib = lib % tuple(words)

print (lib)
