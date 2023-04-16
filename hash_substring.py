# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    actionChoose = input()
    if  "i" in actionChoose.lower():        
    # input from keyboard
        n = int(input())
        data = list(map(int, input().split()))

    elif "f" in actionChoose.lower():
        openFilename = input()
        if "a" in openFilename.lower():
            return
        else:
            with open("./tests/" + openFilename, mode = "r") as f:
                # input from keyboard
                n = int(f.readline())
                data = list(map(int, f.readline().split()))
          else:
            return
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 

    # and return an iterable variable
    return [0]


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

