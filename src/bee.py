import api

ashrlmuser = api.User("ashrlm", "Smiles987")
ashrlmuser.api.login()
script = []
ashrlmuser.api.searchUsername("ashrlm")
ashrlmuser.usr_pk = ashrlmuser.usr.api.LastJson["user"]["pk"]


with open("bee.txt") as beefile:
    for line in beefile:
        if line=="\n":
            continue
        [script.append(word.replace("\n", "")) for word in line.split(" ")]

for word in script:
    ashrlmuser.sendMessage(8618824054, word)
