age_input = raw_input()
inputdata = raw_input()


inputlist = inputdata.split()
numbers = [long(i) for i in inputlist]
maximum=0;
count = 0;
for x in numbers:
    if (x > maximum):
        maximum = x
for x in numbers:
    if (x == maximum):
        count = count+1
print count;


