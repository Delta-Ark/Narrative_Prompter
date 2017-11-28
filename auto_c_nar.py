import requests
import re
bank = []
words = []

#search the relations of the concept net, and clean them
def search_relations():
    page = 20
    #search relations
    while page < int(limit):
        obj = requests.get("http://api.conceptnet.io/c/en/" +str(input)+ "?offset=" + str(page) + "&limit=20").json()
        for i in range(len(obj['edges'])):
            bank.append(obj['edges'][i]["@id"])
        page = page + 20
    #clean relations
    for i in range(len(bank)):
        bank[i] = bank[i].replace('/c/en/', '')
        bank[i] = bank[i].replace('a/[/r/', '')
        bank[i] = bank[i].replace('/', '')
        bank[i] = bank[i].replace(']', '')
        new = bank[i].split(",")
        print new[2],
        print new[0],
        print new[1]

#search for specific relations, and clean them
def search_specific():
    page = 20
    #search specific relations
    while page < int(limit):
        obj = requests.get("http://api.conceptnet.io/c/en/" +str(input)+ "?offset=" + str(page) + "&limit=20").json()
        for i in range(len(obj['edges'])):
            if result in obj['edges'][i]["@id"]:
                bank.append(obj['edges'][i]["@id"])
        page = page + 20
    #clean relations
    for i in range(len(bank)):
        bank[i] = bank[i].replace('/c/en/', '')
        bank[i] = bank[i].replace('a/[/r/', '')
        bank[i] = bank[i].replace('/', '')
        bank[i] = bank[i].replace(']', '')
        new = bank[i].split(",")
        print new[2],
        print new[0],
        print new[1]

#loop
loop = 1
while loop == 1:

#search specific relations (!)
#only english (!)

    #prompter
    input = raw_input("term: ")
    limit = raw_input("limit: (40+)")
    print "/r/RelatedTo /r/IsA /r/PartOf /r/HasA /r/UsedFor /r/CapableOf /r/AtLocation /r/Causes"
    print "/r/HasSubevent /r/HasFirstSubevent /r/HasLastSubevent /r/HasPrerequisite /r/HasProperty"
    print "/r/MotivatedByGoal /r/ObstructedBy /r/Desires /r/CreatedBy /r/Synonym /r/Antonym"
    print "/r/DerivedFrom /r/SymbolOf /r/DefinedAs /r/Entails /r/MannerOf /r/LocatedNear /r/HasContext"
    result = raw_input("general or enter specific relation: ")
    if result == "general":
        search_relations()
    if result != "general":
        search_specific()

    bank = []

    #adder
    final_input = raw_input("select: ")
    words.append(final_input),

    #shower
    print words

    #exiter
    if input == "  ":
        print " "
        print " ".join(words)
        print " "
        loop = 0
