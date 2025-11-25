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


def getTree(frequencies):
    tree = []
    #frequencies.reverse()   # rectified so that we get the lowest value first
    while len(frequencies) > 1:
        for i in range(1, len(text)):
            tree.append((frequencies[i], frequencies[i]))  # adding the least 2 
            frequencies.pop(frequencies[i])    #removing the least 2                       #NOT WORKING  
            frequencies.pop(frequencies[i+1])                                              #NOT WORKING    
    return tree, frequencies

print(getFrequencies(sortList(getTree(text))))