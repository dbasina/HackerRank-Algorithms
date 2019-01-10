alice= raw_input();
bob = raw_input();
alice_list=alice.split()
bob_list = bob.split()
points=[0,0]


for x in range(len(alice_list)):
   
    if (int(alice_list[x]) > int(bob_list[x])):
        points[0]=points[0]+1
    
    if (int(alice_list[x]) < int(bob_list[x])):
        points[1]= points[1]+1
        
        
print points[0],points[1];