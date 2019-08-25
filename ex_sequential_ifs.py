def resolveListCommands(lines):
	
    response = []
    
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
        
        if command == "insert":
            list.insert(number, index)
        elif command == "remove":
            list.remove(number)
        elif command == "sort":
            list.sort()
        elif command == "pop":
            list.pop()
        elif command == "reverse":
            list.reverse()
        elif command == "append":
            list.append(number)
        elif command == "print":
            response.append(f'{list}')
    
    return response