f = open('Day 7/input.txt')

folderStructure = {}
currentPath = []

while True:
    command = f.readline()[:-1]

    if not command:
        break

    if command[0:4] == '$ cd':
        action = command.split(' ')
        if action[2] == '/':
            currentPath = []
        elif action[2] == '..':
            currentPath.pop(-1)
        else:
            currentPath.append(action[2])
            folderStructure['/'.join(currentPath)] = 0
    elif command[0:4] == '$ ls':
        pass
    elif command[0:4] == 'dir ':
        pass
    elif command.split(' ')[0].isnumeric():
        file = command.split(' ')
        if '/'.join(currentPath) in folderStructure:
            folderStructure['/'.join(currentPath)] += int(file[0])
        else:
            folderStructure['/'.join(currentPath)] = int(file[0])

sortOrder = sorted(folderStructure, reverse=True,
                   key=lambda x: len(x.split('/')))

folderStructure = {k: folderStructure[k]
                   for k in sortOrder if k in folderStructure}

total = 0

for folder in folderStructure:
    total += folderStructure[folder]
print(total)


for folder in folderStructure:
    parrentFolder = folder.split('/')
    parrentFolder.pop(-1)
    parrentFolder = '/'.join(parrentFolder)
    if parrentFolder in folderStructure:
        folderStructure[parrentFolder] += folderStructure[folder]

potentialFolders = []

for folder in folderStructure:
    if folderStructure[folder] >= 30000000-(70000000-total):
        potentialFolders.append(folderStructure[folder])
potentialFolders.sort()
print(potentialFolders[0])
