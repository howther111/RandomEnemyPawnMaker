import CreateMachineNumber
import CreatePetName

petname = CreatePetName.CreatePetName()
machinenumber = CreateMachineNumber.CreateMachineNumber()

f = open('petname.txt', 'w')
f.write(petname)
f.close()

f = open('petnamelist.txt', 'a')
f.write(petname + "\n")
f.close()

f = open('machinenumber.txt', 'w')
f.write(machinenumber)
f.close()

f = open('machinenumberlist.txt', 'a')
f.write(machinenumber + "\n")
f.close()

f = open('fullmachinename.txt', 'w')
f.write(machinenumber + " " + petname)
f.close()

f = open('fullmachinenamelist.txt', 'a')
f.write(machinenumber + " " + petname + "\n")
f.close()