unmmp = input("Name and extension of unmimified file: ")
mmp = input("Name and extension of mimipied file: ")
with open(unmmp) as entry, open(mmp, 'w') as exit: 
        for line in entry.readlines():
            line = line.replace('\n', '')
            exit.write(line)
entry.close()
line.close()
