inputdata = raw_input();
inputlist = inputdata.split()
numbers = [long(i) for i in inputlist]
numbers.sort()
minsum = 0
maxsum =0

counter =0
while counter<4:
    minsum = minsum + numbers[counter]
    counter = counter + 1

counter = 4
while counter>0:
    maxsum = maxsum + numbers[counter]
    counter = counter-1

print minsum,maxsum
    