def resolveListCommands(lines):
    
    response = []
    
    dic = {
     "insert" : lambda list, number, index : list.insert(number, index),
     "remove" : lambda list, number, index : list.remove(number),
     "sort"   : lambda list, number, index : list.sort(),
     "pop"    : lambda list, number, index : list.pop(),
     "reverse": lambda list, number, index : list.reverse(),
     "append" : lambda list, number, index : list.append(number),
     "print"  : lambda list, number, index : response.append(f'{list}')
    }

    list = []
    for phase in lines:
        line = phase.split(' ')
        command = line[0]
        number = 0
        index = 0
        if len(line) > 1:
            number = int(line[1])
        if len(line) > 2:
            index = int(line[2])
        
        dic[command](list, number, index)
    
    return response