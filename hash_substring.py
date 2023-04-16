# python3
B = 26
Q = 256

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
      actionChoose = input()
    if  "i" in actionChoose.lower():        
    # input from keyboard
        patternInput = input()
        textData = input()

    elif "f" in actionChoose.lower():
        openFilename = input()
        if "a" in openFilename.lower():
            return
        else:
            with open("./tests/" + openFilename, mode = "r") as f:
                # input from keyboard
                patternInput = f.readline()
                textData = f.readline()
    else:
        return
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    return (patternInput.rstrip(), textData.rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_hash(pattern)-> int:
    global B, Q
    patternLength = len(pattern)
    hashResult = 0
    for i in range(patternLength):
        hashResult = (B * hashResult + ord(pattern[i])) % Q
    return hashResult

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    result = []
    patternLength = len(pattern)    
    paternHashResult = get_hash(pattern)
    textDataLength = len(text)
    
    for i in range(0, textDataLength - patternLength + 1):
        textDataHashResult = get_hash(text[i: i + patternLength])
        if paternHashResult == textDataHashResult:
            if pattern == text[i: i + patternLength]:
                result.append(i)
    # and return an iterable variable
    return result


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

