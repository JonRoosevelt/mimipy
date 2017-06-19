with open('entry.txt') as entry, open('exit.txt', 'w') as exit: 
        for line in entry.readlines():
            line = line.replace('\n', '')
            exit.write(line)
entry.close()
line.close()
