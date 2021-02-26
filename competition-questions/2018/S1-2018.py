n = int(input()) 
pos = [] 
size = 9999999999.0 
smaller = 9999999999.0 

for i in range(0,n): 
    pos.append(float(input())) 

pos.sort() 

    
for i in range(1,n - 1): 
    smaller = (((pos[i] - pos[i-1]))/2) + ((pos[i+1] - pos[i])/2) 
    if smaller < size: 
        size = smaller 
print(size)
