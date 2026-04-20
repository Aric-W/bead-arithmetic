dict = {'0': "=O|=||OOOOO=",
        '1': "=O|=O||OOOO=",
        '2': "=O|=OO||OOO=",
        '3': "=O|=OOO||OO=",
        '4': "=O|=OOOO||O=",
        'F': "=O|=OOOOO||=",
        '5': "=|O=||OOOOO=",
        '6': "=|O=O||OOOO=",
        '7': "=|O=OO||OOO=",
        '8': "=|O=OOO||OO=",
        '9': "=|O=OOOO||O=",
        'T': "=|O=OOOOO||=",
        "=O|=||OOOOO=": '0',
        "=O|=O||OOOO=": '1',
        "=O|=OO||OOO=": '2',
        "=O|=OOO||OO=": '3',
        "=O|=OOOO||O=": '4',
        "=O|=OOOOO||=": 'F',
        "=|O=||OOOOO=": '5',
        "=|O=O||OOOO=": '6',
        "=|O=OO||OOO=": '7',
        "=|O=OOO||OO=": '8',
        "=|O=OOOO||O=": '9',
        "=|O=OOOOO||=": 'T'} 

dictNM = {
        '0': ['= ',' O ',' | ',  '= ', ' | ',' | ',' O ', ' O ', ' O ', ' O ', ' O ', '= '],
        '1': ['= ',' O ',' | ',  '= ', ' O ',' | ',' | ', ' O ', ' O ', ' O ', ' O ', '= '],
        '2': ['= ','O', ' | ',  '= ', 'O','O',' | ', ' | ', 'O', 'O', 'O', '= '],
        '3': ['= ','O', ' | ',  '= ', 'O','O','O', ' | ', ' | ', 'O', 'O', '= '],
        '4': ['= ','O', ' | ',  '= ', 'O','O','O', 'O', ' | ', ' | ', 'O', '= '],
        'F': ['= ','O', ' | ',  '= ', 'O','O','O', 'O', 'O', ' | ', ' | ', '= '],
        '5': ['= ',' | ', 'O',  '= ', ' | ',' | ', 'O', 'O', 'O', 'O', 'O', '= '],
        '6': ['= ',' | ', 'O',  '= ','O',' | ', ' | ', 'O', 'O', 'O', 'O', '= '],
        '7': ['= ',' | ', 'O',  '= ','O','O', ' | ', ' | ', 'O', 'O', 'O', '= '],
        '8': ['= ',' | ', 'O',  '= ','O','O', 'O', ' | ', ' | ', 'O', 'O', '= '],
        '9': ['= ',' | ', 'O',  '= ','O','O', 'O', 'O', ' | ', ' | ', 'O', '= '],
        'T': ['= ',' | ', 'O',  '= ','O','O', 'O', 'O', 'O', ' | ', ' | ', '= '],
}

def display(list, nM=False):
        if(nM):
            compact = []
            rows = ["","","","","","","","","","","","","","",""]
            total = ""

            if len(list) > 0:
                for c in list:
                    compact.append(dictNM.get(c))

                for j in range (0,12):
                    for k in range (0,len(compact)):
                        rows[j] = rows[j] + compact[k][j]
                        if (k < len(compact)-1):
                            rows[j] = rows[j]

                for i in range(0,12):
                    total = total + rows[i] + "\n"

    
            return total
        compact = []
        rows = ["","","","","","","","","","","","","","",""]
        total = ""

        if len(list) > 0:
            for c in list:
                compact.append(dict.get(c))

        for j in range (0,12):
            for k in range (0,len(compact)):
                rows[j] = rows[j] + compact[k][j]
                if j == 0 or j == 3 or j == 11:
                    rows[j] = rows[j] + "="
                elif (k < len(compact)-1):
                    rows[j] = rows[j] + " "

        for i in range(0,12):
            total = total + rows[i] + "\n"


        #print(total)
        return total

def flipBook(list, nM = False):
    states = []

    for c in list:
        states.append(display(c, nM))

    return states
