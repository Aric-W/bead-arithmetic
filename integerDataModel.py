import abacusClass1 as ab
import random as r
mT = [["00","00","00","00","00","00","00","00","00","00"],
          ["00","01","02","03","04","05","06","07","08","09"],
          ["00","02","04","06","08","10","12","14","16","18"],
          ["00","03","06","09","12","15","18","21","24","27"],
          ["00","04","08","12","16","20","24","28","32","36"],
          ["00","05","10","15","20","25","30","35","40","45"],
          ["00","06","12","18","24","30","36","42","48","54"],
          ["00","07","14","21","28","35","42","49","56","63"],
          ["00","08","16","24","32","40","48","56","64","72"],
          ["00","09","18","27","36","45","54","63","72","81"]]
order = {'0': 0,
             '1': 1,
             '2': 2,
             '3': 3,
             '4': 4,
             '5': 5,
             'F': 5,
             '6': 6,
             '7': 7,
             '8': 8,
             '9': 9,
             'T': 10}
def convertToRegNum(st):
        arr = []
        for c in st:
            arr.append(c)

    
        if arr[0] == "0" and len(arr) > 1:
            arr.pop(0)
            return convertToRegNum(arr)
        else:
        
            return arr
def stringize(arr):
    res = ""
    for c in arr:
        res = res + c
    return res

def atLeastHowMany(num):
    largest = ""
    rods = len(num)
    if rods == 1:
        return "This number can be represented by at least 1 rod."
    
    tray = ab.abacus(rods)

    for i in range(0,rods-1):
        largest = largest + "1"
    largest = largest + "0"

    if largest == "10":
        return "This number can be represented by at least 1 rod."

    tray.set(num)
    ineq = tray.compare(0,rods,largest)

    if ineq[1] == " > ":
        return "This number can be represented by at least " + str(rods) + " rods"
    else:
        return "This number can be represented by at least " + str(rods-1) + " rods"
    
def adiro(addend1, addend2):
    displaySize = max(8,max(len(addend1),len(addend2))) + 1

    display = ab.abacus(displaySize)

    display.set(addend1)

    end_val = len(addend2)-1

    states = []
    lis = []
    for c in display.backingList:
        lis.append(c)
    states.append(lis)

# Create the range object and sample all elements from it
    randomRods = r.sample(range(end_val + 1), k=end_val + 1)

    iS = [] #iS might go into this loop rather than outside of it.
    for c in randomRods:
        off = displaySize - len(addend2)
        states = states + display.add(addend2[c],off+c,True,False)
    #print(stringize(convertToRegNum(display.value(0,displaySize)[1])))    
    return states, stringize(convertToRegNum(display.value(0,displaySize)[1]))

def sudiro(minuend, subtrahend):
    displaySize = max(8,max(len(minuend),len(subtrahend))) + 1

    display = ab.abacus(displaySize)

    display.set(minuend)

    end_val = len(subtrahend)-1

    states = []
    lis = []
    for c in display.backingList:
        lis.append(c)
    states.append(lis)

    if display.compare(0,displaySize,subtrahend)[1] == " < ":
        return states
    else:
        randomRods = r.sample(range(end_val + 1), k=end_val + 1)
        print(randomRods) #when 1 is at randomRods[0] there is an error
        #randomRods = [1,2,0]
        #display.numberOfRods-len(subtrahend) needs to be changed?
        #if (display.compare(0,display.numberOfRods,subtrahend)[1] == " = " or display.compare(0,display.numberOfRods,subtrahend)[1] == " > ") and display.backingList[display.numberOfRods-len(subtrahend)] == "0":
        #        states = states + display.clearRods(0,display.numberOfRods)

        iS = [] #iS might go into this loop rather than outside of it.
        for c in randomRods:
            
            off = displaySize - len(subtrahend)
            
            
            print(off)
            states = states + display.subt(subtrahend[c],off+c)
        
            
        return states, stringize(convertToRegNum(display.value(0,displaySize)[1]))
#this doesnt work?
#I cant trust this to do what I want.
def placeDec(num, loc):

    place = len(num)-loc
    arrayed = []
    for i in range(0,place):
        arrayed.append(num[i])
   
    arrayed.append('.')

    for i in range(place,len(num)):
        arrayed.append(num[i])

    newVal = ""

    for c in arrayed:
        newVal = newVal + c

    return newVal    
def prepForModMultJPS(plier, plicand,getRidOfLeading0s=True,sp=2): #plier = 67, plicand = 345
    multiplierIndices = []
    multiplicandIndices = []

    if(getRidOfLeading0s):
        plier = stringize(convertToRegNum(plier))
        plicand = stringize(convertToRegNum(plicand))

    '''for i in range(0,len(plier)):
        multiplierIndices.append(i) #multiplierIndices = [0,1]
    for j in range(len(plier)+2,len(plicand)+len(plier)+2):
        multiplicandIndices = [j] + multiplicandIndices #multiplicandIndices = [6,5,4]
    traySize = len(plier) + 2 + len(plicand) + len(plier) + 1 #traySize = 2 + 2 + 3 + 2 + 1 = 10'''

    for i in range(0,len(plier)):
        multiplierIndices.append(i) #multiplierIndices = [0,1]
    for j in range(len(plier)+1,len(plicand)+len(plier)+1):
        multiplicandIndices = [j] + multiplicandIndices #multiplicandIndices = [6,5,4]
    traySize = len(plier) + 1 + len(plicand) + len(plier) + 1 #traySize = 2 + 2 + 3 + 2 + 1 = 10

    '''for i in range(0,len(plier)):
        multiplierIndices.append(i) #multiplierIndices = [0,1]
    for j in range(len(plier)+sp,len(plicand)+len(plier)+sp):
        multiplicandIndices = [j] + multiplicandIndices #multiplicandIndices = [6,5,4]
    traySize = len(plier) + sp + len(plicand) + len(plier) + sp #traySize = 2 + 2 + 3 + 2 + 1 = 10'''
    tray = ab.abacus(traySize)

    tray.set(plier,0)

    #tray.set(plicand,len(plier)+2)
    tray.set(plicand,len(plier)+1)
    return tray, multiplierIndices, multiplicandIndices, plicand, plier

def multJPS(plier,plicand,getRidOfLeading0s=True,plierDecIndex=0,plicandDecIndex=0, sp=2):
    newIndexOfDecimalPoint = plicandDecIndex + plierDecIndex

    states = []
    triple = prepForModMultJPS(plier,plicand,getRidOfLeading0s,sp)
    lis = []
    for c in triple[0].backingList:
        lis.append(c)
    states.append(lis)
    prods = []
    pp = triple[2][0] + 1
    plicand = triple[3]
    plier = triple[4]
    productLength = len(plier) + len(plicand)
    for c in triple[2]:
        for d in triple[1]:
            
            prods.append(mT[order.get(triple[0].value(c,1)[1])][order.get(triple[0].value(d,1)[1])])
        for e in range(pp,pp+len(prods)):
            states = states + triple[0].add(prods[e-pp],e)
            
        prods = []
        pp = pp-1
        triple[0].set("0",pp)
        lis = []   
        for c in triple[0].backingList:
            lis.append(c)
        states.append(lis)
    val = ""
    # should be
    # for i in range(len(plier) + 3 + 1,len(plier) + 3 + 1 + productLength):?
    #the problem is that it gets the value one rod at a time
    #for i in range(len(plier) + 3,len(plier) + 3 + productLength):
    #    val = val + triple[0].value(i,1)[1]
    #val = triple[0].value(len(plier) + 3,len(plier) + 3 + productLength-(len(plier) + 3))[1]
    val = triple[0].value(len(plier) + 2,len(plier) + 2 + productLength-(len(plier) + 2))[1]
    #val = triple[0].value(len(plier) + sp + 1,len(plier) + sp + 1 + productLength-(len(plier) + sp + 1))[1]
    #return stringize(convertToRegNum(val))
    #print(stringize(convertToRegNum(val)))
    #gets rid of the leading 0s
    #what happens if we dont call convertToRegNum?
    #return stringize(convertToRegNum(val)), states
    if val[0] == '0':
        val2 = ''
        for i in range(1,len(val)):
            val2 = val2 + val[i]
    else:
        val2 = val
    if newIndexOfDecimalPoint != 0:
        val2 = placeDec(val2,newIndexOfDecimalPoint)
    return stringize(convertToRegNum(val2)), states
    
def prepForMultCNS(plier, plicand): #plier = 67, plicand = 345
    multiplierIndices = []
    multiplicandIndices = []

    '''for i in range(0,len(plicand)): 
        multiplicandIndices = [i] + multiplicandIndices #multiplicandIndices = [2,1,0]
    for j in range(len(plicand)+len(plier) + 2,len(plicand)+len(plier) + 2 + len(plier)):
        multiplierIndices.append(j) #multiplierIndices = [8,9]
    traySize = len(plier) + 2 + len(plicand) + len(plier) #traySize = 2 + 2 + 3 + 2 + 1 = 10'''

    for i in range(0,len(plicand)): 
        multiplicandIndices = [i] + multiplicandIndices #multiplicandIndices = [2,1,0]
    for j in range(len(plicand)+len(plier) + 1,len(plicand)+len(plier) + 1 + len(plier)):
        multiplierIndices.append(j) #multiplierIndices = [8,9]
    traySize = len(plier) + 1 + len(plicand) + len(plier) #traySize = 2 + 2 + 3 + 2 + 1 = 10

    '''for i in range(0,len(plicand)): 
        multiplicandIndices = [i] + multiplicandIndices #multiplicandIndices = [2,1,0]
    for j in range(len(plicand)+len(plier),len(plicand)+len(plier) + len(plier)):
        multiplierIndices.append(j) #multiplierIndices = [8,9]
    traySize = len(plier) + len(plicand) + len(plier) #traySize = 2 + 2 + 3 + 2 + 1 = 10'''

    tray = ab.abacus(traySize)

    tray.set(plicand,0)

    #tray.set(plier,len(plicand) + len(plier)+2)
    tray.set(plier,len(plicand) + len(plier)+1)
    

    return tray, multiplierIndices, multiplicandIndices

def MultCNS(plier,plicand):
    states = []
    triple = prepForMultCNS(plier,plicand)
    lis = []
    for c in triple[0].backingList:
        lis.append(c)
    states.append(lis)
    prods = []
    pp = triple[2][0] + 1
    ppFirst = pp
    productLength = len(plier) + len(plicand)
    for c in triple[2]:
        for d in triple[1]:
            val1 = order.get(triple[0].value(c,1)[1])
            val2 = order.get(triple[0].value(d,1)[1])
            prods.append(mT[val1][val2])
        for e in range(pp,pp+len(prods)):
            states = states + triple[0].add(prods[e-pp],e)
            
        prods = []
        pp = pp-1
        triple[0].set("0",pp)
        lis = []   
        for c in triple[0].backingList:
            lis.append(c)
        states.append(lis)
    ppLast = pp
    val = ""
    #for i in range(1,productLength+1):
    #    val = val + triple[0].value(i,1)[1]
    val = triple[0].value(1,productLength)[1]

    #return stringize(convertToRegNum(val))
    print(stringize(convertToRegNum(val)))

    #return stringize(convertToRegNum(val)), states
    return stringize(convertToRegNum(val)),states

def convertToRegNum(st):
        arr = []
        for c in st:
            arr.append(c)

    
        if arr[0] == "0" and len(arr) > 1:
            arr.pop(0)
            return convertToRegNum(arr)
        else:
        
            return arr

def correctDigits(terms):
    firstIdx = -1
    for i in range(0, len(terms)):
        if len(terms[i]) == 2:
            firstIdx = i
            break

    if firstIdx == -1:
        return terms
    terms[firstIdx-1] = str(int(terms[firstIdx-1][0]) + int(terms[firstIdx][0]))
    terms[firstIdx] = terms[firstIdx][1]
    return correctDigits(terms)

def napiersBones(number, zeroThrough10):
    nB = [[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
      [[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7],[0,8],[0,9]],
      [[0,0],[0,2],[0,4],[0,6],[0,8],[1,0],[1,2],[1,4],[1,6],[1,8]],
      [[0,0],[0,3],[0,6],[0,9],[1,2],[1,5],[1,8],[2,1],[2,4],[2,7]],
      [[0,0],[0,4],[0,8],[1,2],[1,6],[2,0],[2,4],[2,8],[3,2],[3,6]],
      [[0,0],[0,5],[1,0],[1,5],[2,0],[2,5],[3,0],[3,5],[4,0],[4,5]],
      [[0,0],[0,6],[1,2],[1,8],[2,4],[3,0],[3,6],[4,2],[4,8],[5,4]],
      [[0,0],[0,7],[1,4],[2,1],[2,8],[3,5],[4,2],[4,9],[5,6],[6,3]],
      [[0,0],[0,8],[1,6],[2,4],[3,2],[4,0],[4,8],[5,6],[6,4],[7,2]],
      [[0,0],[0,9],[1,8],[2,7],[3,6],[4,5],[5,4],[6,3],[7,2],[8,1]]] 
    
    if (zeroThrough10 == "10"):
        l = []
        for i in range(0,len(number)):
            l.append(number[i])
        if l[0] == '0':
            #del digits[0]
            l.pop(0)
        

        l = l + ['0']
        return l
    else:
        idx = int(zeroThrough10)
        
        pairs = []
        terms = []
        terms.append(str(nB[idx][int(number[0])][0]))
        for i in range(1,len(number)):
            x = nB[idx][int(number[i-1])]
            #pairs.append(x)
            y = nB[idx][int(number[i])]
            #pairs.append(y)
            terms.append(str(nB[idx][int(number[i-1])][1] + nB[idx][int(number[i])][0]))
            #print(terms)
        final = nB[idx][int(number[len(number)-1])]  
        terms.append(str(final[1]))
        #terms.append(str(nB[single][int(multi[len(multi)-1])][1]))
        
        correctDigits(terms)
        
    return convertToRegNum(terms)#,pairs
    #return terms

def chunkTable(num):
    firstNonzeroIndexFound = False
    quant = ""
    for i in range(0,len(num)):
        if(num[i] != "0"):
            firstNonzeroIndexFound = True
        if firstNonzeroIndexFound:
            quant = quant + num[i]
    table = []
    for i in range(0,11):
        table.append(napiersBones(quant,str(i)))
    return table

def firstNonnegNumber(idx,arr):
    if idx >= len(arr)-1:
        return 0
    elif arr[idx] != "0":
        return idx
    else:
       return firstNonnegNumber(idx+1,arr)

def division(dividend, divisor,extra=11, dontPutDecimal=False):
    digCount = 1
    decimalPlaced = False
    listOfBoxes = []
    states = []
    lis = []
    quotient = ""

    tray = ab.abacus(len(dividend)+extra)

    
    tray.set(dividend,0)
    for c in tray.backingList:
        lis.append(c)
    states.append(lis)
    if convertToRegNum(dividend) == "0":
        return [],"0",[lis.copy(),['$','0','0'],list(lis)]
    elif convertToRegNum(divisor) == "0":
        return "err", "err","err"

    unitRod = len(dividend)-1
    relevant = len(divisor)+2

    cT = chunkTable(divisor)
    #might not need this offset thing
    #offset = False

    #print(cT)

    start = 0
    if len(divisor) >= len(dividend):
        end = len(dividend)
    else:
        end = len(divisor) + 1

    
    while(True):
        box = []
        if end > tray.numberOfRods or (tray.compare(start,end-start,"0")[1] == ' = ' and end > unitRod+1):
            break



        if tray.compare(start,end-start,cT[10])[1] == ' > ' or tray.compare(start,end-start,cT[10])[1] == ' = ':
            end = end-1
            offset = True

        #for i in range (0,tray.numberOfRods):
        for i in range(start,end):
            box.append(tray.backingList[i])
        
        
        for i in range(0,10):
            #print(tray.compare(start,end-start,cT[i]))
            #print(tray.compare(start,end-start,cT[i+1]))
            #so the problem is that start should not increment
            if (tray.compare(start,end-start,cT[i])[1] == ' > ' or tray.compare(start,end-start,cT[i])[1] == ' = ') and (tray.compare(start,end-start,cT[i+1])[1] == ' < '):
                break
        digCount = digCount + 1
        quotient = quotient + str(i)
        states.append(['$',quotient,str(i)])
        #testing code ----> print(tray.backingList)
        if len(cT[i]) < end-start:
            
            #states.append("write " + str(digCount) + "th digit")
            #states.append("subtract " + stringize(cT[i]) + " at " + str(start+1))
            states = states + tray.subt(cT[i],start+1)
            
        else:
            #states.append("write " + str(digCount) + "th digit")
            #states.append("subtract " + stringize(cT[i]) + " at " + str(start))
            states = states + tray.subt(cT[i],start)
            
        #digCount = digCount + 1
        #quotient = quotient + str(i)
        
        if not decimalPlaced and end > unitRod and not dontPutDecimal:
            #states.append("write '.' ")
            quotient = quotient + '.'
            decimalPlaced = True

        #if end-start == relevant:
        #    start = start+1
        '''if offset:
            #end = end+2
            end = end + 1
            offset = False
            #print(tray.backingList)
            #I might be able to move this out, since I do it any way
            if tray.backingList[start] == '0':
                start = start + 1
        

        else:
            end = end + 1
            #I really need to fix this tomorrow, the problem is what if we're trying to find 779/777 = 1.00257...
            # [7,7,9,0,0,0,0,0,0,0,0,0,0,0,0] divided by 777
            #the second iteration the tray is [0,0,2,0,0,0,0,0,0,0,0,0,0,0,0]
            #and we want to increment the start
            #
            #print(tray.backingList)
            if tray.backingList[start] == '0':
                start = start + 1'''
        
        end = end + 1
        if tray.backingList[start] == '0':
                start = start + 1
        

        
        listOfBoxes.append(box)
        err = tray.value(0,tray.numberOfRods)[1]

    quot2 = ""
    if(quotient[len(quotient)-1] == '.'):
        for i in range(0,len(quotient)-1):
            quot2 = quot2 + quotient[i]
        return listOfBoxes,quot2, states, err, unitRod,
    else:
        return listOfBoxes,quotient,states, err, unitRod

'''def convertToRegNum(st):
        arr = []
        for c in st:
            arr.append(c)

    
        if arr[0] == "0" and len(arr) > 1:
            arr.pop(0)
            return convertToRegNum(arr)
        else:
        
            return arr

def correctDigits(terms):
    firstIdx = -1
    for i in range(0, len(terms)):
        if len(terms[i]) == 2:
            firstIdx = i
            break

    if firstIdx == -1:
        return terms
    terms[firstIdx-1] = str(int(terms[firstIdx-1][0]) + int(terms[firstIdx][0]))
    terms[firstIdx] = terms[firstIdx][1]
    return correctDigits(terms)'''

def napiersBonesForSqrt(number, zeroThrough10):
    nB = [[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
      [[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7],[0,8],[0,9]],
      [[0,0],[0,2],[0,4],[0,6],[0,8],[1,0],[1,2],[1,4],[1,6],[1,8]],
      [[0,0],[0,3],[0,6],[0,9],[1,2],[1,5],[1,8],[2,1],[2,4],[2,7]],
      [[0,0],[0,4],[0,8],[1,2],[1,6],[2,0],[2,4],[2,8],[3,2],[3,6]],
      [[0,0],[0,5],[1,0],[1,5],[2,0],[2,5],[3,0],[3,5],[4,0],[4,5]],
      [[0,0],[0,6],[1,2],[1,8],[2,4],[3,0],[3,6],[4,2],[4,8],[5,4]],
      [[0,0],[0,7],[1,4],[2,1],[2,8],[3,5],[4,2],[4,9],[5,6],[6,3]],
      [[0,0],[0,8],[1,6],[2,4],[3,2],[4,0],[4,8],[5,6],[6,4],[7,2]],
      [[0,0],[0,9],[1,8],[2,7],[3,6],[4,5],[5,4],[6,3],[7,2],[8,1]]] 
    
    nBsqrt = [[0,0],[0,1],[0,4],[0,9],[1,6],[2,5],[3,6],[4,9],[6,4],[8,1],[10,0]]
    
    if (zeroThrough10 == "10"):
        l = []
        for i in range(0,len(number)):
            l.append(number[i])
        if l[0] == '0':
            #del digits[0]
            l.pop(0)
        

        #l = l + ['0']
        return l + ['1'] + ['0']
    else:
        idx = int(zeroThrough10)
        
        pairs = []
        terms = []
        terms.append(str(nB[idx][int(number[0])][0]))
        for i in range(1,len(number)):
            x = nB[idx][int(number[i-1])]
            #pairs.append(x)
            y = nB[idx][int(number[i])]
            #pairs.append(y)
            terms.append(str(nB[idx][int(number[i-1])][1] + nB[idx][int(number[i])][0]))
            #terms.append(nBsqrt[idx][1] + nBsqrt[idx][0])
            #print(terms)
        final = nB[idx][int(number[len(number)-1])]  
        terms.append(str(final[1]))
        terms.append(str(nBsqrt[idx][0]) + str(nBsqrt[idx][1]))
        #terms.append(str(nB[single][int(multi[len(multi)-1])][1]))
        
        correctDigits(terms)
        
    return convertToRegNum(terms)#,pairs
    #return terms
#completes the square
def chunkTableForSqrt(num):
   
    firstNonzeroIndexFound = False
    quant = ""
    for i in range(0,len(num)):
        if(num[i] != "0"):
            firstNonzeroIndexFound = True
        if firstNonzeroIndexFound:
            quant = quant + num[i]
    table = []
    for i in range(0,11):
        table.append(napiersBonesForSqrt(quant,str(i)))

    return table

'''def firstNonnegNumber(idx,arr):
    if idx >= len(arr)-1:
        return 0
    elif arr[idx] != "0":
        return idx
    else:
       return firstNonnegNumber(idx+1,arr)'''
    
def sqrt(sqr,rods=12):
    flag = []
    digCount = 1
    states = []
    lis = []
    err = ""
    
    twoab = ""
    root = ""
    rootNoDec = ""
    
    tray = ab.abacus(len(sqr) + rods)
    tray.set(sqr,0)
    for c in tray.backingList:
        lis.append(c)
    if sqr =="0":
        return "0", "0",[lis.copy(),['$', '0', '0', ''],list(lis)],'0',0
    states.append(lis)
    start=0
    if len(sqr) % 2 == 0:
        end = 2
    else:
        end = 1
    unitRod = len(sqr)-1
    decimalPlaced = False
    cT = ["0","1","4","9","16","25","36","49","64","81"]



    while(True):
        if end > tray.numberOfRods or (tray.compare(start,end-start,"0")[1] == ' = ' and end > unitRod+1):
            break

        
        for i in range(0,10):
            #print(tray.compare(start,end-start,cT[i]))
            #print(tray.compare(start,end-start,cT[i+1]))
            if (tray.compare(start,end-start,cT[i])[1] == ' > ' or tray.compare(start,end-start,cT[i])[1] == ' = ') and (tray.compare(start,end-start,cT[i+1])[1] == ' < '):
                break
        #print(tray.value(0,tray.numberOfRods)[1])
        #print(i,cT[i])
        digCount = digCount + 1
        root = root + str(i)
        rootNoDec = rootNoDec + str(i)
        states.append(['$',root,str(i),twoab])
        twoab = multJPS("2",rootNoDec)[0]
        
        if len(cT[i]) < end-start:
           
           #states.append("write " + str(digCount) + "th digit")
           #states.append("subtract " + stringize(cT[i]) + " at " + str(start+1))
           states = states + tray.subt(cT[i],start+1)
           
           #tray.subt(cT[i],start+1)
        else:
           
           #states.append("write " + str(digCount) + "th digit")
           #states.append("subtract " + stringize(cT[i]) + " at " + str(start))
           states =  states + tray.subt(cT[i],start)
        
           #tray.subt(cT[i],start)
        #print(tray.value(0,tray.numberOfRods)[1])
        #print(i,cT[i])
        #digCount = digCount + 1
        #root = root + str(i)
        #rootNoDec = rootNoDec + str(i)
        if not decimalPlaced and end > unitRod:
            #states.append("write '.' ")
            root = root + '.'
            decimalPlaced = True
        #maybe should be renamed to twob
        #return final twob, we need final len(twob) + 3 labels
        #for division we need len(divisor)+2 labels
        #twoab = multJPS("2",rootNoDec)[0]
        cT = chunkTableForSqrt(twoab)
        
        end = end + 2
        if tray.backingList[start] == '0':
            start = firstNonnegNumber(start,tray.backingList)
    #sqrt("123456789",0) err will be 8
    #I need to change this, it should take the value of the whole
    #set of rods and record the unit rod and those two together
    #will tell the user what the remainder is
    #like 8 is the unit rod it should return
    #err and uR, in this case err will be 000002468 and
    #uR will be 8 so the err will be 2468
    #err = tray.value(unitRod,tray.numberOfRods-unitRod)[1]
    err = tray.value(0,tray.numberOfRods)[1]
    


    rt2 = ""
    if(root[len(root)-1] == '.'):
        for i in range(0,len(root)-1):
            rt2 = rt2 + root[i]
        return rt2, err,states,len(twoab),unitRod
    else:
        return root, err,states,len(twoab),unitRod    

def countLeading0s(input):
    counter = 0
    for c in input:
        if c == "0":
            counter = counter + 1
        else:
            break
    return counter
def fibo(sz):
    seq = "1, 1, "
    num = int(sz)
    if num < 9 or (num)%2 == 0:
        return 0
    
    freeRod = int((num-1)/2)
    
    tray = ab.abacus(num)
    states = []
    lis = []
    terms = ["1"]
    #print("['1']")
    tray.set("1",freeRod-1)

    tray.set("1")
    for c in tray.backingList:
        lis.append(c)
    states.append(['$',seq])
    states.append(lis)
    
    limit = ""
    for i in range(0,int((num-1)/2 - 1)):
        limit = limit + "9"
    flipper = 0
    while(True):
        rightVal = tray.value(0,freeRod)[1]
        noLeading0sRightVal = convertToRegNum(rightVal)
        rightLeading0sCount = countLeading0s(rightVal)

        leftVal = tray.value(freeRod+1,freeRod)[1]
        noLeading0sLeftVal = convertToRegNum(leftVal)
        leftLeading0sCount = countLeading0s(leftVal)
        if flipper % 2 == 0:
            states = states + tray.add(noLeading0sLeftVal,0+leftLeading0sCount,True,True)
            #seq = seq + stringize(convertToRegNum(tray.value(freeRod+1,freeRod)[1])) + ', '
            seq = seq + stringize(convertToRegNum(tray.value(0,freeRod)[1])) + ', '
            terms.append(noLeading0sLeftVal)
            #print(noLeading0sLeftVal)
        else:
            #change the magic number 5 to something
            #states = states + tray.add(noLeading0sRightVal,5+rightLeading0sCount)

            states = states + tray.add(noLeading0sRightVal,freeRod+1+rightLeading0sCount,True,True)
            #seq = seq + stringize(convertToRegNum(tray.value(0,freeRod)[1])) + ', '
            seq = seq + stringize(convertToRegNum(tray.value(freeRod+1,freeRod)[1])) + ', '
            terms.append(noLeading0sRightVal)
            #print(noLeading0sRightVal)
        #change the magic numbers 4 and 5 to something
        #if(tray.compare(0,4, limit)[1] == " > " or tray.compare(5,4, limit)[1] == " > "):
        if(tray.compare(0,freeRod, limit)[1] == " > " or tray.compare(freeRod+1,freeRod, limit)[1] == " > "):
            if(tray.compare(0,freeRod, limit)[1] == " > "):
                #seq = seq + tray.value(0,freeRod)[1]
                terms.append(tray.value(0,freeRod)[0])
                break
            elif(tray.compare(freeRod+1,freeRod, limit)[1] == " > "):
                #seq = seq + tray.value(freeRod+1,freeRod)[1]
                terms.append(tray.value(freeRod+1,freeRod)[0])
                break
            
        flipper =  flipper + 1
        #a display label will display every element of the sequence in order
        #as the sequence is generated, when a ['$'] is hit, the next element will appear
        #will start out with the first two elements: 1, 1,
        states.append(['$',seq])
    states.append(['$',seq])
    return states,terms

    

def reverseFibo(sz):
    num = int(sz)
    #go backwards through terms
    terms = fibo(sz)[1]

    freeRod = int((num-1)/2)

    tray = ab.abacus(num)
    leftStart = terms[len(terms)-1]
    rightStart = terms[len(terms)-2]

    #print(leftStart, rightStart)

    seq = ""
    seq = seq + stringize(leftStart) + ', ' + stringize(rightStart) + ', '
    

    #the bigger number is on the left
    tray.set(leftStart,freeRod-1-len(leftStart)+1)

    tray.set(rightStart)

    #seq = seq + stringize(tray.value(freeRod-1-len(leftStart)+1,len(leftStart))[0])
    
    states = []
    lis = []
    for c in tray.backingList:
        lis.append(c)
    states.append(['$',seq])
    states.append(lis)

    flipper = 0
    while(True):
        #leftVal, rightVal, first
        rightVal = tray.value(0,freeRod)[1]
        noLeading0sRightVal = convertToRegNum(rightVal)
        rightLeading0sCount = countLeading0s(rightVal)

        leftVal = tray.value(freeRod+1,freeRod)[1]
        noLeading0sLeftVal = convertToRegNum(leftVal)
        leftLeading0sCount = countLeading0s(leftVal)
        if(tray.compare(0,freeRod, "1")[1] == " = " and tray.compare(freeRod+1,freeRod, "1")[1] == " = "):
            break
        if flipper % 2 == 0:
            #find the first nonzero index of the minuend
            for i in range(0,freeRod):
                if tray.backingList[i] != '0':
                    break
            #put a copy of the backing list after filling rods?
            #I think subt basically already does that
            #tray.fillRods(i,freeRod-i,[],True)
            #seq = seq + stringize(noLeading0sLeftVal) + ', '
            #seq = seq + stringize(convertToRegNum(tray.value(0,freeRod)[1])) + ', '
            states = states + tray.subt(noLeading0sLeftVal,0+leftLeading0sCount,True)
            seq = seq + stringize(convertToRegNum(tray.value(0,freeRod)[1])) + ', '
            #seq = seq + stringize(noLeading0sLeftVal) + ', '
            
            
        else:
            for i in range(freeRod,len(tray.backingList)):
                if tray.backingList[i] != '0':
                    break
            #tray.fillRods(i,len(tray.backingList)-i,[],True)
            #seq = seq + stringize(noLeading0sRightVal) + ', '
            #seq = seq + stringize(convertToRegNum(tray.value(freeRod+1,freeRod)[1])) + ', '
            states = states + tray.subt(noLeading0sRightVal,freeRod+1+rightLeading0sCount,True)
            seq = seq + stringize(convertToRegNum(tray.value(freeRod+1,freeRod)[1])) + ', '
            #seq = seq + stringize(noLeading0sRightVal) + ', '
            
        flipper = flipper + 1
        #will do the same as in fibo but in reverse.
        states.append(['$',seq])
    #states[len(states)-1][1] = states[len(states)-1][1] + "1"
    return states
 #both are strings, can return a negative integer
def minus(minuend, subtrahend):
        minu = len(minuend)
        sutr = len(subtrahend)
        '''if(minu > sutr):
            tray = ab.abacus(minu+1)
            tray.set(minuend)
        else:
            tray = ab.abacus(sutr+1)
            tray.set(subtrahend)'''

        ext = max(8,max(minu,sutr)) + 1

        #tray = ab.abacus(minu+1)
        tray = ab.abacus(ext)
        tray.set(minuend)
        

        
        

        #trip = tray.compare(0,minu+1,subtrahend)
        trip = tray.compare(0,ext,subtrahend)

        greater = ""
        lesser = ""
        res = []
        if trip[1] == " < ":
            tray.clear()
            #tray = ab.abacus(sutr+1)
            #tray.set(subtrahend)
            greater = subtrahend
            lesser = minuend
            res = res + ["-"]
        else:
            greater = minuend
            lesser = subtrahend
            
        states = []
        lis = []
        tray.set(greater)
        for c in tray.backingList:
            lis.append(c)
        states.append(lis)
        states = states + tray.subt(lesser)
            #remember that you're working with negative numbers so put the - back on
            #123 - 999 is also -999 + 123
            
        
        
        res = res + convertToRegNum(tray.value(0, tray.numberOfRods)[0])

        return states,stringize(res)

#integ1 and integ2 are strings
def sum(integ1,integ2):
    #both are negative, take the - off, add them and then put the - back on
    if integ1[0] == "-" and integ2[0] == "-":
        i1 = ""
        i2 = ""
        for i in range(1,len(integ1)):
            i1 = i1 + integ1[i]

        for i in range(1,len(integ2)):
            i2 = i2 + integ2[i]
        summ ="-" + adiro(i1,i2)[1]
    elif integ1[0] == "-":
        i1 = ""
        for i in range(1,len(integ1)):
            i1 = i1 + integ1[i] 
        summ = minus(integ2,i1)[1]
    elif integ2[0] == "-":
        i2 = ""
        for i in range(1,len(integ2)):
            i2 = i2 + integ2[i] 
        summ = minus(integ1,i2)[1]
    else:
        summ = adiro(integ1,integ2)[1]

    return summ
    
def regAdd(addend1, addend2):
    testSize = max(8,max(len(addend1),len(addend2))) + 1
    test = ab.abacus(testSize)
    test.set(addend1)
    test.add(addend2)
    
    displaySize = max(8,max(len(addend1),len(addend2))) 

    display = ab.abacus(displaySize)

    
    print(test.compare(0,testSize,display.maxNum))
    if test.compare(0,testSize,display.maxNum)[1] == ' > ':
        displaySize = displaySize + 1
        del display
        display = ab.abacus(displaySize)

    del test

    display.set(addend1)
    


    states = []
    lis = []
    for c in display.backingList:
        lis.append(c)
    states.append(lis)

    states = states + display.add(addend2)
      
    return states, stringize(convertToRegNum(display.value(0,displaySize)[1]))