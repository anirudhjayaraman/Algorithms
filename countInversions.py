# load contents of text file into a list
# numList
NUMLIST_FILENAME = "IntegerArray.txt"
inFile = open(NUMLIST_FILENAME, 'r')

with inFile as f:
    numList = [int(integers.strip()) for integers in f.readlines()]

total = 0

def countSplitInversions(a,b):
    """ Function to calculate the total number of inversions in an unsorted array. """
    global total
    c = []
    splitInversions = 0
    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
            splitInversions += len(a)            
    total += splitInversions
    if len(a) == 0:
        c += b
    else:
        c += a
    return c, total

def inversions(x):
    """ Function to calculate the number of split inversions between two sorted arrays. """
    global total
    if len(x) == 0 or len(x) == 1:
        return x, 0
    else:
        middle = len(x)/2
        a = inversions(x[:middle])[0]
        b = inversions(x[middle:])[0]
        return countSplitInversions(a,b)

# call function and output number of inversions
print inversions(numList)[1]