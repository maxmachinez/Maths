"""#huffman coding
text = str(input("Enter what you would like to encode:"))

def getFrequencies(text): #gets all da frequencies of da letters
    frequencies = []
    for i in text:
        if (i, text.count(i)) not in frequencies: # idk why this is the only thing which works but ok
            frequencies.append((i, text.count(i)))
        if (i, text.count(i)) in frequencies:  # to avoid it going like [h, 1], [h, 2] ... etc
            continue

    return frequencies

def sortList(frequencies):
    frequencies.sort(key=lambda x: x[1]) # cool lambda thingy
    #frequencies.reverse()               # will rectify this later
    return frequencies

def getTree(oList):
    tree = []
    while len(oList) > 1: 
        oList.sort(key=lambda x: x[1])  
        tree += [oList[0:2]] 
        combinedFreq = oList[0][1] + oList[1][1]  
        combinedLetter = oList[0][0] + oList[1][0]
        oList = oList[2:]  
        oList.append((combinedLetter, combinedFreq))  
        print(oList)
        
                                                          #  tempList = []
                                                          #  fv = oList[i]
                                                          #  print(fv)
                                                          #  tempList.append(fv)                           #later
                                                          #  try: tempList.append(oList[i + 1])
                                                          #  except: break
                                                          #  tree.append(tempList)
    print(tree)
getTree(sortList(getFrequencies(text)))

def encode(frequency):
    code = dict()
    #for i in txt:
    #    if i in code:
    #         
"""
#huffman coding
text = str(input("Enter what you would like to encode:"))

def getFrequencies(text): #gets all da frequencies of da letters
    frequencies = []
    for i in text:
        if (i, text.count(i)) not in frequencies: # idk why this is the only thing which works but ok
            frequencies.append((i, text.count(i)))
        if (i, text.count(i)) in frequencies:  # to avoid it going like [h, 1], [h, 2] ... etc
            continue

    return frequencies

def sortList(frequencies):
    frequencies.sort(key=lambda x: x[1]) # cool lambda thingy
    #frequencies.reverse()               # will rectify this later
    return frequencies

def getTree(oList):
    tree = []
    bl = True
    tmpAp = oList[0]
    while len(oList) > 1: 
        oList.sort(key=lambda x: x[1])  
        tree += [oList[0:2]] 
        combinedFreq = oList[0][1] + oList[1][1]  
        combinedLetter = oList[0][0] + oList[1][0]
        oList = oList[2:]  
        oList.append((combinedLetter, combinedFreq))  
        if bl:
            tmpAp = combinedLetter, " ", combinedFreq, " - ", "1"
            tree.append(tmpAp)
            bl = False
        if not bl:
            tmpAp = combinedLetter, " ", combinedFreq, " - ", "0"
            tree.append(tmpAp)
        print(oList)

        
        
                                                          #  tempList = []
                                                          #  fv = oList[i]
                                                          #  print(fv)
                                                          #  tempList.append(fv)                           #later
                                                          #  try: tempList.append(oList[i + 1])
                                                          #  except: break
                                                          #  tree.append(tempList)
    print(tree)
getTree(sortList(getFrequencies(text)))



def encode(frequency):
    code = dict()


    

                
            
        


        

