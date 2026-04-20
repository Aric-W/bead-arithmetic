#in this new version of the abacus class we are trying to use fillRods and clearRods more precisely
class abacus:
    backingList = []
    numberOfRods = 0
    justCleared = False
    preCleared = []
    maxNum = ""

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
    
    #this is only for strings.
    #so this doesn't need interimStates
    def convertToRegNum(self,arr,interimStates=[]):

    
        if arr[0] == "0" and len(arr) > 1:
            arr.pop(0)
            return self.convertToRegNum(arr)
        else:
        
            return arr
    def prepareForSubt(self,arr,interimStates=[]):
        state = []
        for c in arr:
            state.append(c)
        interimStates.append(state)
        firstIdxNonZero = -1
        for i in range(0,len(arr)):
            if arr[i] != '0':
                firstIdxNonZero = i
                break
        if(firstIdxNonZero < 0):
            #print("all zero!")
            return
    
        firstIdx = -1
        for i in range(firstIdxNonZero+1,len(arr)):
            if arr[i] == '0':
                firstIdx = i
                break

            
        if(firstIdx < 0):
            return
        if(arr[firstIdx-1] == 'T'):
            arr[firstIdx] = 'T'
            arr[firstIdx-1] = '9'
        #cant do it this way
        #elif arr[firstIdx] == '0':
        #    return
        else:
            arr[firstIdx] = 'T'
            arr[firstIdx-1] =str(self.order.get(arr[firstIdx-1])-1)
        self.prepareForSubt(arr,interimStates)

    def convertToDec(self,arr,interimStates=[]):
        state = []
        for c in arr:
            state.append(c)
        interimStates.append(state)
        for i in range(0,len(arr)):
            if (arr[i] == "F"):
                arr[i] = '5'
        firstIdx = -1
        #the abacus needs at least 2 rods
        for i in range(1,len(arr)):
            if arr[i] == 'T' and arr[i-1] != 'T':
                firstIdx = i
                break
            
        if(firstIdx < 0):
            return
        elif self.order[arr[firstIdx-1]] == 9:
            arr[firstIdx - 1] = 'T'
            arr[firstIdx] = '0'
        else:
            arr[firstIdx - 1] = str(self.order[arr[firstIdx-1]]+1)
            arr[firstIdx] = '0'
        
        self.convertToDec(arr, interimStates)

    
    def __init__(self,numRods):
        fill = []
        fill2 = []
        mn = []
        for i in range (0,numRods):
            fill.append('0')
            fill2.append('0')
        self.backingList = fill
        self.numberOfRods = numRods
        self.preCleared = fill2
        for i in range (0,numRods):
            mn.append("T")
        mn = ["0"] + mn
        self.convertToDec(mn)
        for i in range(0, len(mn)):
            self.maxNum = self.maxNum + mn[i]

    #elsewhere num will be checked so that it's in the proper form
    #(only Ts, Fs, and digits) When I implement kijohou I will allow 
    #for Qs and such
    def set(self,num, idx = "NA"):
        if(idx == "NA"):
            idx = self.numberOfRods - len(num)
        else:
            idx = int(idx)
        
        if len(num) > self.numberOfRods:
            return 
        elif len(num) + idx > self.numberOfRods:
            return
        elif (idx + len(num) == self.numberOfRods):
            for i in range(0,len(num)):
                self.backingList[idx+i] = num[i]
        else:
            for i in range(0,len(num)):
                self.backingList[idx+i] = num[i]
            #return
        self.justCleared = False

        state = []
        for c in self.backingList:
            state.append(c)
        return [state], state

    #should remove leading 0s? No
    def value(self,idx,numRods,arr = []):
        if len(arr) == 0:

            if (idx + numRods > len(self.backingList)):
                return
            if (idx < 0) or numRods > len(self.backingList) or numRods < 1:
                return 
            startIdx = idx
            endIdx = idx + numRods
            printOut = ""
            copy = []
            for i in range(startIdx,endIdx):
                copy.append(self.backingList[i])

            copy = ['0'] + copy 
            self.convertToDec(copy) #value clears out the Ts

            if copy[0] == "0":
                copy.pop(0)
            for i in range (0,len(copy)):
                printOut = printOut + copy[i]
        
        return copy, printOut

    
    #RHS becomes LHS and arr becomes RHS?
    def compare(self, idx, numRods, RHS, arr=[]):
        if (idx + numRods > len(self.backingList)):
            return
        if (idx < 0) or numRods > len(self.backingList) or numRods < 1:
            return 
        startIdx = idx
        endIdx = idx + numRods
        RHSCopy = []
        RHS1 = []
        for i in range(0,len(RHS)):
            RHSCopy.append(RHS[i])
            RHS1.append(RHS[i])
        LHS = []
        LHSCopy = []
        if(startIdx != endIdx):
            for i in range(startIdx,endIdx):
                LHS.append(self.backingList[i])
                LHSCopy.append(self.backingList[i])
        else:
            LHS.append(self.backingList[startIdx])
            LHSCopy.append(self.backingList[startIdx])
        triple = [LHSCopy, " < ",RHSCopy]
    
        maxLen = len(RHS)

        if (len(LHS) > len(RHS)):
            maxLen = len(LHS) 
            for i in range(0,maxLen-len(RHS)):
                RHS1 = ["0"] + RHS1
        else:
            for i in range(0,maxLen-len(LHS)):
                LHS = ["0"] + LHS
        LHS = ['0'] + LHS
        RHS1 = ['0'] + RHS1
        self.convertToDec(LHS)
        self.convertToDec(RHS1)
        for i in range(0,maxLen+1):
            if(self.order.get(LHS[i]) > self.order.get(RHS1[i])):
                triple[1] = " > "
                return triple
            elif(self.order.get(LHS[i]) < self.order.get(RHS1[i])):
                return triple
        triple[1] = " = "
        return triple
    
    #this could provide states for animation
    def clear(self):
        for i in range(0, self.numberOfRods):
            self.preCleared[i] = self.backingList[i]

        for i in range (0, self.numberOfRods):
            self.set('0',i)
        
        
        self.justCleared = True
    
    #I need a more general undo method that will undo
    #the most recent operation
    def undoClear(self):
        if self.justCleared:
            for i in range(0, self.numberOfRods):
                self.set(self.preCleared[i],i)
            
        self.justCleared = False    
        return
    
    def appendRod(self):
        self.backingList.append('0')
        self.numberOfRods = self.numberOfRods + 1
    #prependRod
    def prependRod(self):
        self.backingList = ['0'] + self.backingList
        self.numberOfRods = self.numberOfRods + 1

    def delRodRight(self):
        self.backingList.pop()
    
    def delRodLeft(self):
        self.backingList.pop(0)

    #compare one digit with two digits 
    #return 2 if you need to fill
    #1 if you need to clear
    #0 if neither
    #this method exists because in the previous version of this class
    #errors came mostly from aodttd and sodftd, so this method
    #will determine if a particular pair of rods needs to be cleared
    #or filled before we call aodttd or sodftd
    def codwtd(self,od,td):
        #td[0] might be T for example
        firstDig = str(self.order.get(td[0])) + "0"
        secDig = str(self.order.get(td[1]))

        twoDig = int(firstDig) + int(secDig)
        if od == 'T':
            oneDig = 10
        else:
            oneDig = int(od)

        sum = twoDig+oneDig
        #fill if return 2 this will be the check for subt and reverseFibo
        if twoDig < oneDig:
            return 2
        #clear if return 1 this will be the check for add
        # if comp == 1:
        #else:
        #
        #check if we can clear
        #then use codwtd
        #then clear
        #elif sum > 110:
        elif sum > 110:
            return 1
        else: 
            return 0
    #should give no errors
    def aodttd(self,od,td):
        dub = [td[0],td[1]]
        if td[0] == 'F':
            dub[0] = '5'
        if td[1] == 'F':
            dub[1] = '5'
        td = dub
        #td is copied when it's passed in?
        if(td[1] == 'T' and td[0] == 'T'):
            addend1 = 110
        elif td[0] == 'T':
            addend1= int("10" + td[1])
        elif td[1] == 'T':
            addend1 = int(str(int(td[0]) + 1) + '0')
        else:
            addend1 = int(td[0] + td[1])
        if od == 'T':
            addend2 = 10
        else:
            addend2 = int(od)
        sum = addend1+addend2
        
      
        res = str(sum)

        if len(res) == 3 and res[1] != '1':
            res = 'T' + res[2]
        elif len(res) == 3 and res[1] == '1':
            res = "TT"
        elif len(res) == 1:
            res = '0' + res[0]
    
        if res[0] == '5' and td[0] == '4':
            res = 'F' + res[1]

        return res
    #should give no errors
    def sodftd(self,od,td,specialRules = True):
        #I prefer the results that this logic gives me, should I have something 
        #similar for aodttd?
        #this condition is optional, but I think I should have it.
        if od == "0":
            return td
        
        dub = [td[0],td[1]]
        if td[0] == 'F':
            dub[0] = '5'
        if td[1] == 'F':
            dub[1] = '5'
        td = dub
        #td is copied when it's passed in?
        if(td[1] == 'T' and td[0] == 'T'):
            minuend = 110
        elif td[0] == 'T':
            minuend = int("10" + td[1])
        elif td[1] == 'T':
            minuend = int(str(int(td[0]) + 1) + '0')
        else:
            minuend = int(td[0] + td[1])
        if od == 'T':
            subtrahend = 10
        else:
            subtrahend = int(od)
        dif = minuend-subtrahend
        
        
        res = str(dif)


        if len(res) == 3:
            if res[2] == '5':
                res = 'T' + 'F'
            else:
                #maybe change this so that if res[2] == "0"
                #res = '9' + 'T? Seriously consider that.
                if res[2] == '0':
                    res = '9' + 'T'
                else:
                    res = 'T' + res[2]
        elif len(res) == 2 and res[1] == "0" and specialRules:
            res = str(int(res[0]) - 1) + 'T'
        elif len(res) == 2 and res[1] == "5" and specialRules:
            res = str(int(res[0])) + 'F'
        elif len(res) == 1:
            if res == '5':
                res = '0' + 'F'
            else:
                res = '0' + res[0]
            
    
        return res
       
    #if this returns a False we will have subt return an error message
    #first check

    def canSubt(self,num,idx="NA",start=0):
        
        if idx == "NA":
            idx = self.numberOfRods - len(num)
        if len(num) > self.numberOfRods:
            return False
        elif len(num) + int(idx) > self.numberOfRods:
            return False
        idx = int(idx)
        if start > idx:
            return False
        #what does compare do again if start == idx?
        #compare takes numRods and wont allow numRods < 1
        trip = self.compare(start,idx+len(num),num)
    
        if trip[1] == " > " or trip[1] == " = ": 
            return True
        else:
            return False
    #this is for add
    #will from the index will check if there is a non-T to the left of idx
    #idx should be an int   
    def canMakeRoom(self,idx,endIdx=0):
        if endIdx > idx:
            return False
        if (idx + 1 > self.numberOfRods):
            return False
        if (idx < 0):
            return False
        startIdx = idx
        

        clearTill = -1
        i = 0
        while(True):
            if self.backingList[startIdx-i] != "T":
                clearTill = startIdx-i
                break
            i = i + 1
            if (i+endIdx > startIdx):
                break
        
        if clearTill < 0:
            return False
        else:
            return True
    #idx is an int
    #should have an endIdx like canMakeRoom
    def canTake(self,idx,endIdx=0):
        if (idx + 1 > self.numberOfRods):
            return
        if (idx < 0):
            return 
        startIdx = idx
        #endIdx = idx + 2
    

        clearTill = -1
        i = 0
        while(True):
            if self.backingList[startIdx-i] != "0":
                clearTill = startIdx-i
                break
            i = i + 1
            if (i+endIdx > startIdx):
                break
        
        if clearTill < 0:
            return False
        else:
            return True
    #will check if what is on the abacus looks smaller without being so 
    #when I call this in subt the idx will stay the same  
    #checks for a specific situation, nothing is 
    #going wrong if False is returned, but we will turn num into a list
    # and use prepareForSubt on that list and subt that 
    #second check for subt, we wont use clear if this returns True
    #this idx will be an int 
    #we dont clear because we dont want to mess with
    #the abacus, num will be one digit
    #I can return a double (bool, newIdx)
    #will then call clear in subt at newIdx
    def canClearForSubt(self,num,idx):
        

        #0 is the left end of abacus
        
        '''if self.order.get(num[0]) == self.order.get(self.backingList[idx]):
            i = idx+1
            while(i <= self.numberOfRods - 1):
              if self.backingList[i] == '0':
                   continue
              else:
                   return False
            return True'''
        
        i=0 
        #print(self.order.get(num[0]) == self.order.get(self.backingList[idx])+1)   
        if self.order.get(num[0]) == self.order.get(self.backingList[idx])+1:
         #it should be a while(True) that breaks when i == self.numRods - 1?
         #for i in range(idx+1,idx+1+len(num)):
         i = idx+1
         #not subscriptable!
         #zeroesCount.append['0']
         
         while(i <= self.numberOfRods - 1):
              if self.backingList[i] == 'T':
                   return True, i
              elif self.backingList[i] == '9':
                   i = i + 1
                   
                   continue
              else:
                   return False, i
         return False, i
              
        else:
            return False, i
        
        
    def canFillForAdd(self,num,idx):
        i=0
           
        if self.order.get(num[0]) + self.order.get(self.backingList[idx]) == 11:
         #it should be a while(True) that breaks when i == self.numRods - 1?
         #for i in range(idx+1,idx+1+len(num)):
         i = idx+1
         #not subscriptable!
         #zeroesCount.append['0']
         
         while(i <= self.numberOfRods - 1):
              if self.backingList[i] == '0':
                   return True, i
              elif self.backingList[i] == '1':
                   i = i + 1
                   
                   continue
              else:
                   return False, i
         return False, i
              
        else:
            return False, i
            
    def clearRods(self, idx, interimStates=[],provideInterimStates=False):
        #should this be returning nothing?
        #idx is the left rod.
        if (idx + 2 > self.numberOfRods):
            return
        if (idx < 0) or idx > self.numberOfRods-2:
            return 
        startIdx = idx #left rod
        endIdx = idx + 2 #to the right of the right rod
        #for the other method arr[startIdx] == '1'
       

        clearTill = -1
        i = 0
        while(True):
            if self.backingList[startIdx-i] != "T":
                #what if there is a T immediately to the left of the 9?
                #canMakeRoom could be called? It's called in add [1,T,9,9,T] -> [2,1,0,0,0]
                #but [T,T,T,9,9,T] -> [T,T,T,T,0,0]
                #that's how we want it to work
                #I think it works in this context
                #
                if self.backingList[startIdx-i] == "9":
                    #if startIdx-i != 0 or self.canMakeRoom(startIdx-i):
                    if startIdx-i != 0 and self.canMakeRoom(startIdx-i):
                        i = i + 1
                        continue
                    else:
                        clearTill = startIdx-i
                        break   
                else:
                    clearTill = startIdx-i
                    break
            i = i + 1
            #maybe when T is at index 0 we could take 0 to endIdx
            if (i > startIdx):
                clearTill = 0
                break
        
        #I have to change this, this could have startIdx being negative, I dont want that
        #Will make sure there is space to clear into before calling clearRods
        #canMakeRoom is for that. Should it be called here? Well, it's called in add
        startIdx = clearTill
        list = []
        
        for i in range(startIdx,endIdx):
            list.append(self.backingList[i])

        self.convertToDec(list,interimStates)
        iS = []
        for k in range(0,len(interimStates)):
            copyOfBackingList = []
        
            for c in self.backingList:
                copyOfBackingList.append(c)
            j = 0
            #endIdx+1
            for i in range(startIdx,endIdx):
                copyOfBackingList[i] = interimStates[k][j]
                j = j + 1
            iS.append(copyOfBackingList)

        j = 0
        #endIdx+1
        for i in range(startIdx,endIdx):
            self.backingList[i] = list[j]
            j = j + 1
        if provideInterimStates:
            return iS
        else:
            li = []
            for c in self.backingList:
                li.append(c)
            return [li]
    #filling two rods at a time is idx the index of the left rod or the right rod
    def fillRods(self, idx,  interimStates = [],provideInterimStates=False):
        if (idx + 2 > self.numberOfRods):
            return
        #idx is the left rod
        if (idx < 0) or idx > self.numberOfRods-2:
            return 
        startIdx = idx
        endIdx = idx + 2 #endIdx = idx + 2
    #for the other method arr[startIdx] == '1'
    #that self.backingList[startIdx] == '1' condition might
    #be getting in the way of division.
    #maybe not.
    #13 starts with a 1 and startIdx != 0


        clearTill = -1
        i=0
        while(True):
            if self.backingList[startIdx-i] != "0":
                if self.backingList[startIdx-i] == "1":
                    #if startIdx-i != 0 or self.canTake(startIdx-i):
                    if startIdx-i != 0 and self.canTake(startIdx-i):
                        i = i + 1
                        continue
                    else:
                        clearTill = startIdx-i
                        break
                else:   
                    clearTill = startIdx-i
                    break
            i = i + 1
            if (i > startIdx):
                clearTill = 0
                break
        #will check if there is anything to fill in before calling this method
        if clearTill > -1:
            startIdx = clearTill
        
        list = []
        
        for i in range(startIdx,endIdx):
            list.append(self.backingList[i])
        #interimStates = []
        self.prepareForSubt(list,interimStates)
        iS = []
        '''copyOfBackingList = []
        
        for c in self.backingList:
            copyOfBackingList.append(c)'''
        
        for k in range(0,len(interimStates)):
            copyOfBackingList = []
        
            for c in self.backingList:
                copyOfBackingList.append(c)
            j = 0
            
            for i in range(startIdx,endIdx):
                copyOfBackingList[i] = interimStates[k][j]
                j = j + 1
            iS.append(copyOfBackingList)

        j = 0
        for i in range(startIdx,endIdx):
            self.backingList[i] = list[j]
            j = j + 1
        if provideInterimStates:
            return iS
        else:
            li = []
            for c in self.backingList:
                li.append(c)
            return [li]
    
  
    #this idx will be an int
    def canIAddThis(self,num, idx ,turnOffClearRods=False):
        
        
        dummy = abacus(self.numberOfRods+1)
        
        
        if len(num) > self.numberOfRods:
            return False
        elif len(num) + idx > self.numberOfRods:
            return False
        for i in range(1,len(self.backingList)+1):
            #dummy.append( self.backingList[i])
            dummy.set(self.backingList[i-1],i)
        #dummy = ["0"] + dummy
        dummy.set("0",0)

        #this piece of logic exists because I was getting back True when I put a T at
        #index 0 and then tried to put a 1 at index 0 on a 9-rod abacus. 
        #the 9-rod abacus can hold that number: ['T','T','0','0','0','0','0','0','0']
        #but that's not how you put it on
        #what about the case where [T,T,0,0,0,0,0,0,0] and I try add("1",1)
        #the abacus can hold that as [T,T,T,0,0,0,0,0,0]
        #0 is where dummy's extra digit is at
        #I only need to check the first/largest digit?
        #this should go in the loop?
        #if (idx == 0 or self.backingList[idx-1] == "T") and (dummy.order.get(dummy.backingList[idx+1]) + dummy.order.get(num[0]) > 10):
        #if idx == 0 and dummy.order.get(dummy.backingList[1]) + dummy.order.get(num[0]) > 10:
            #return False

        dindex = idx + 1
        for i in range(0,len(num)):
            #self.canMakeRoom work because we're not adding to self yet
            #maybe canMakeRoom should have to arguments, idx input startIdx = "0"
            #this runs up against adiro 
            #tray.clear()
            #tray.set("987654312")
            #print(tray.add("2",1))
            #print(tray.add("1",0))
            #we should be able to put a T at 1 if there is no room at 0 
            #right adding, if the digit is a 1 and there is a 0 on idx+i+1 put a T at idx+i+1
            #if idx+i+1 < self.numberOfRods-1 and if od==1 and if backingList[idx+i] == T
            #then backingList[idx+i+1] = 1
            #continue
            #put in a boolean that makes this condition automatically false if we're doing adiro
            #if not adiroMode doesnt belong here? should the condition be (dummy.order.get(dummy.backingList[dindex+i]) + dummy.order.get(num[i]) > 10 > 11?
            #Do I need this at all? If I try add("1","1") to [T,T,0,0,0,0] then add should give an error message?
            #if not adiroMode and ( not dummy.canMakeRoom(dindex + i -1,1)) and  (dummy.order.get(dummy.backingList[dindex+i]) + dummy.order.get(num[i]) > 10):
            #if ( not dummy.canMakeRoom(dindex + i -1,1)) and  (dummy.order.get(dummy.backingList[dindex+i]) + dummy.order.get(num[i]) > 11 or not adiroMode):
            if ( not dummy.canMakeRoom(dindex + i -1,1)) and  (dummy.order.get(dummy.backingList[dindex+i]) + dummy.order.get(num[i]) > 11):
                return False
            #double = (dummy[offset + i -1] + dummy[offset + i],num[i])
            #might need a getter when I translate 
            #the code into c++ or something
            double = (dummy.backingList[dindex + i -1] + dummy.backingList[dindex + i],num[i])
            comp = self.codwtd(double[1],double[0])
            if comp == 1:
                #canMakeRoom is necessary because it catches a situation 
                #that would be a problem with clearRods
                secondCheck = dummy.canMakeRoom(idx+i)
                if not secondCheck:
                    return False
                if not turnOffClearRods:
                    #idx is the left rod 
                    dummy.clearRods(idx+i-1,[],True)
                    double = (dummy.backingList[dindex + i -1] + dummy.backingList[dindex + i],num[i])
            res = dummy.aodttd(double[1], double[0])
            #add will be the one to tell the user if there is an error

            dummy.set(res[0],dindex + i -1)
            dummy.set(res[1],i+dindex)

        if dummy.compare(0,self.numberOfRods+1,self.maxNum)[1] == " > ":
            return False
        else:
            return True
    
    #add will be the method that tells the user if there is an error
    #adding 1 to TT
    #adiroMode will be for turning off that self.canIAddThis(num,idx) check
    #adiro will do the check once on it's own
    def add(self,num, idx = "NA",redundantSteps = True,turnOffClearRods=False):
        states = []
        if(idx == "NA"):
            idx = len(self.backingList) - len(num)
        else:
            idx = int(idx)
        
        #error handling like this will eventually be moved out of the model
        #I have extra error-checking in canIAddThis for some reason.
        if idx < 0:
            print("error!")
            return states
        elif len(num) > self.numberOfRods:
            print("error!")
            return states
        elif len(num) + idx > self.numberOfRods:
            print("error!")
            return states
        

        #the idx that will be passed to canIAddThis will be an int
        #if not adiroMode belongs here, it should be a default False arg for add
        #adiro will call canIAddThis on the right addend.
        #adiroMode is really only for this
        #I dont think I need adiroMode
        if( not self.canIAddThis(num,idx)):
            print("error!")
            return states
        #I cant do it this way, but trying it showed me there's a serious bug in prepareForSubt
        #special case where self.order.get(self.backingList[idx]) + self.order.get(num) == 11 and 
        #self.order.get(backingList[idx+1]) == 0 then self.fillRods(idx)
        #trying it this way revealed a bug that I might not have otherwise caught
        #praise be to God!
        #if adiroMode:
        #    self.fillRods(idx)
        #all this complicated logic... 
        #Do I need a method that prepareForSubts a predetermined section of the abacus?
        #for adiro mode each digit will be passed in one at a time.
        adi = self.canFillForAdd(num,idx)
        #if adiroMode:
        if adi[0] and not self.canMakeRoom(idx-1): #and idx-2 > 0 and idx < self.numberOfRods-1 and self.backingList[idx-2] == 'T' and (self.backingList[idx+1] != "1" or self.backingList[idx+1] != "0"):
                states = states + self.fillRods(adi[1]-1,[],True)
                
                '''i = 0

                while(idx + i + 1 < self.numberOfRods):
                    lsit = []
                    for c in self.backingList:
                        lsit.append(c)
                    print(lsit)
                    if self.order.get(self.backingList[idx+i+1]) == 0:
                        self.fillRods(idx+i)
                        break
                    i = i + 1
                if self.order.get(self.backingList[idx]) + self.order.get(num) == 11 and idx+1 < self.numberOfRods and self.order.get(self.backingList[idx+1]) == 0:
                    self.fillRods(idx)

            lsit = []
            for c in self.backingList:
                lsit.append(c)
            print(lsit)'''
    
                
        #shouldnt it be len(num)?
        #for i in range(0, self.numberOfRods):
        for i in range(0,len(num)):

            if idx+i == 0:
                double = ("T" + self.backingList[idx+i],num[0])
            else:
                double = (self.backingList[idx + i -1] + self.backingList[idx + i],num[i])
            if double[1] == '0' and not redundantSteps:
                    continue
            comp = self.codwtd(double[1],double[0])
            
            if comp == 1:
                #idx+i-1 if we're adding at numberOfRods-1?, idx+i otherwise
                #if we are adding at 0, 0 is treated as the right rod
                #idx+i if idx = 0 and idx+i-1 otherwise We want left rod unless there is no left rod
                #there is no left rod at 0
                secondCheck = self.canMakeRoom(idx+i)
                if not secondCheck:
                    print("error!")
                    return states
                #or if idx+i != 1 or idx+i != 0 
                #[0,T,T,0,0,0] 
                #idx + i == 2
                if not turnOffClearRods and idx+i != 1:
                    #idx+i is the right rod
                    states = states + self.clearRods(idx+i-1,[],True)
                if idx + i -1 < 0:
                    double = ("T" + self.backingList[idx + i],num[i])
                else:
                    double = (self.backingList[idx + i -1] + self.backingList[idx + i],num[i])
                    #double[0] and res will be compared to figure out the hand movements
                    #i+idx is the place: double[0] = 59 (9 at idx-i=7) res=62.  59 = ['5','1','4'] 62 = ['6','0','2']
                    #"slide one 10 up one 5 up and two 1s down at 7 "
            res = self.aodttd(double[1], double[0])
            if idx+i == 0:
                self.backingList[i+idx] = res[1]
            else:
                self.backingList[idx + i -1] = res[0]
                self.backingList[i+idx] = res[1]
            lis = []
            for c in self.backingList:
                lis.append(c)
            states.append(lis)
        return states
    
    def subt(self,num, idx = "NA",redundantSteps = True,turnOffFillRods=False,turnOffClearRods=False):
        states = []
        if(idx == "NA"):
            idx = len(self.backingList) - len(num)
        else:
            idx = int(idx)
        
        #error handling like this will eventually be moved out of the model
        if idx < 0:
            print("error!")
            return states
        elif len(num) > self.numberOfRods:
            print("error!")
            return states
        elif len(num) + idx > self.numberOfRods:
            print("error!")
            return states
        else:
            #should idx here just be idx?
            #it just happens to work with idx="NA"
            #subt("52",2) on [0,0,5,1,9,9,9,T,0]
            #subt("523",2) on [0,0,5,2,2,9,9,T,0]
            if not self.canSubt(num,idx):
               firstCheck = self.canClearForSubt(num[len(num)-1],idx+len(num)-1)
               if not firstCheck[0]:
                   print("error!")
                   return states
            
        i = 0
        lenny = len(num)  
        #cant change the range within the loop  
        #for i in range(0,lenny):
        #lenny shouldnt be changed here
        #for i in range (0,len(num)) is clearer
        while(i < lenny):

            if idx+i == 0:
                double = ("0" + self.backingList[idx+i],num[0])
            else:
                double = (self.backingList[idx + i -1] + self.backingList[idx + i],num[i])
            if double[1] == '0' and not redundantSteps:
                    i=i+1
                    continue
            comp = self.codwtd(double[1],double[0])
            
            secondCheck = self.canClearForSubt(double[1],idx+i)
            if comp == 2:
                #should num or double[1] be the first argument?
                #I want to use prepareForSubt on the first digit of num
                
                
                if secondCheck[0] and not turnOffClearRods:
                    #doing it this way (prepare the subtrahend for subt) seems to involve
                    #too much messing around with indices 
                    '''newForm = []
                    newForm.append(double[1])
                    for c in zeroesCount:
                        newForm.append("0")
                    self.prepareForSubt(newForm,[])
                    num = newForm
                    lenny = len(newForm)'''
                    #prepare the minuend for subt with clearRods
                    #secondCheck[1]-1 is a left rod
                    states = states + self.clearRods(secondCheck[1]-1,[],True)
                #I dont like this third check, get rid of zeroesCount
                #thirdCheck = self.canClearForSubt(double[1],idx+i,zeroesCount)
                #if thirdCheck[0]:
                #       states = states + self.clearRods(thirdCheck[1],[],True)
                #what about if subt("52",4) on [0,1,0,0,0,1,9,9,T]? 
                if not turnOffFillRods and not secondCheck[0]:
                    #if we pass idx+i into canTake then we get true if 
                    #there is a nonzero at idx+i is that a problem?
                    #what if we have [T,T,T,T,0,1] and 
                    #we do tray.subt("5") fillRods gets passed idx+i-1 = 4
                    #canTake returns True if a nonzero is found to the left of 
                    #idx+i
                    if(self.canTake(idx+i)) and idx+i != 1 :
                        #remember how this works
                        #if we have [3,7,4,5,0,1]
                        #tray.subt("18",1) will subt to start 37 - 1 then 64 - 8
                        # idx + 0 = 1 then idx + 1 = 2, you cant fill at 0 or -1
                        #[1,0,0,0,0,0] idx+i=2 
                        states = states + self.fillRods(idx+i-1,[],True)
                #it's wrapping around
                if idx + i - 1 < 0:
                    double = ("0" + self.backingList[idx + i],num[i])
                else:
                    double = (self.backingList[idx + i -1] + self.backingList[idx + i],num[i])
                if double[1] == '0' and not redundantSteps:
                    i = i + 1
                    continue
            res = self.sodftd(double[1], double[0])
            if idx+i == 0:
                self.backingList[i+idx] = res[1]
            else:
                self.backingList[idx + i -1] = res[0]
                self.backingList[i+idx] = res[1]
            lis = []
            for c in self.backingList:
                lis.append(c)
            states.append(lis)
            i=i+1
        return states
    
    #both are strings, can return a negative integer
def minus(self,minuend, subtrahend):
        minu = len(minuend)
        sutr = len(subtrahend)

        tray = abacus(minu+1)
        tray.set(minuend)

        trip = tray.compare(0,minu+1,subtrahend)

        res = []
        if trip[1] == " < ":
            del tray
            tray = abacus(sutr+1)
            tray.set(subtrahend)
            tray.subt(minuend)
            #remember that you're working with negative numbers so put the - back on
            #123 - 999 is also -999 + 123
            res = res + ["-"]
        else:
            tray.subt(subtrahend)
        
        res = res + self.convertToRegNum(tray.value(0, tray.numberOfRods)[0])

        return self.stringize(res)


        
    
