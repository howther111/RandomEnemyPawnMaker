import CreatePilotName

firstname = CreatePilotName.CreatePilotName()
lastname = CreatePilotName.CreatePilotName()

f = open('firstname.txt', 'w')
f.write(firstname)
f.close()

f = open('firstnamelist.txt', 'a')
f.write(firstname + "\n")
f.close()

f = open('lastname.txt', 'w')
f.write(lastname)
f.close()

f = open('lastnamelist.txt', 'a')
f.write(lastname + "\n")
f.close()

f = open('fullpilotname.txt', 'w')
f.write(firstname + "・" + lastname)
f.close()

f = open('fullpilotnamelist.txt', 'a')
f.write(firstname + "・" + lastname + "\n")
f.close()